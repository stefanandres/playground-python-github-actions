#!/usr/bin/env python

import unittest
import app as AppClass

class Testing(unittest.TestCase):
  def test_name_setting_true(self):
    test_name = 'test-this-name'
    myapp = AppClass.App(test_name)

    self.assertEqual(myapp.name, test_name)

  def test_name_setting_false(self):
    test_name = 'test-this-name'
    myapp = AppClass.App(test_name)

    self.assertNotEqual(myapp.name, 'should not match')

if __name__ == '__main__':
  unittest.main()

