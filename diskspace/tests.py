from __future__ import print_function
import argparse
import os
import subprocess
import re
import unittest
import diskspace


class TestDiskspace(unittest.TestCase):

   def setUp(self):
      self.cmd = 'du '
      self.abs_directory = os.path.abspath('.')
      self.cmd += self.abs_directory
      self.file_tree = {self.abs_directory: {'print_size': '4.00Mb', 
                                             'children': [], 'size': 8}}
      self.largest_size = 24
      self.total_size = 8


   def test_bytes_to_readable(self):
      t_return = diskspace.test_bytes_to_readable(15986472)
      self.assertEqual(t_return, '7.62Gb')

   def test_subprocess_check_output(self):
      directory = diskspace.subprocess_check_output(self.cmd)
      self.assertIn(self.abs_directory, directory)



if __name__ == '__main__':
   unittest.main()      
