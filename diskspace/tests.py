from __future__ import print_function
import diskspace
import argparse
import sys
import os
import subprocess
import re
import unittest
import StringIO


class TestDiskspace(unittest.TestCase):

      def setUp(self):
            self.cmd = 'du '
            self.abs_directory = os.path.abspath('.')
            self.cmd += self.abs_directory
            self.file_tree = {self.abs_directory: {'print_size': '4.00Mb', 
                                             'children': [], 'size': 8}}
            self.largest_size = 24
            self.total_size = 8

      def test_show_space_list(self):
            capturedOutput = StringIO.StringIO()
            sys.stdout = capturedOutput
            diskspace.show_space_list(diskspace.args.directory, 
                                      diskspace.args.depth,
                                      order=(diskspace.args.order == 'desc'))
            sys.stdout = sys.__stdout__
            self.assertIn('Size (%) File' and self.abs_directory, capturedOutput.getvalue().strip())

      def test_bytes_to_readable(self):
            blocks = 100
            self.assertEqual(diskspace.bytes_to_readable(blocks), "50.00Kb")
      
      def test_bytes_to_readable_none(self):
            blocks = 0
            self.assertEqual(diskspace.bytes_to_readable(blocks),  '0.00B')

      def test_bytes_to_readable_wrong(self):
            blocks = 0
            self.assertNotEqual(diskspace.bytes_to_readable(blocks), "100.0Kb")

      def test_subprocess_check_output(self):
            directory = diskspace.subprocess_check_output(self.cmd)
            self.assertIn(self.abs_directory, directory)

      def test_print_tree(self):
            capturedOutput = StringIO.StringIO()
            sys.stdout = capturedOutput
            diskspace.print_tree(self.file_tree, 
                                 self.file_tree[self.abs_directory], 
                                 self.abs_directory,
                                 self.largest_size,
                                 self.total_size)
            sys.stdout = sys.__stdout__ 
            self.assertEqual('4.00Mb  100%  '+self.abs_directory, capturedOutput.getvalue().strip())




if __name__ == '__main__':
   unittest.main()      
