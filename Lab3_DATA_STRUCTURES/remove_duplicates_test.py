import unittest

class RemoveDuplicatesTestCases(unittest.TestCase):
  def setUp(self):
    self.result1 = remove_duplicates('aaabbbac')
    self.result2 = remove_duplicates('a')
    self.result3 = remove_duplicates('thelexash')

  def test_output_1(self):
    self.assertIsInstance(self.result1, tuple, msg='Incorrect output type')
    self.assertEqual(self.result1, ('abc', 5), msg='Incorrect output')

  def test_output_2(self):
    self.assertIsInstance(self.result2, tuple, msg='Incorrect output type')
    self.assertEqual(self.result2, ('a', 0), msg='Incorrect output')

  def test_output_3(self):
    self.assertIsInstance(self.result3, tuple, msg='Incorrect output type')
    self.assertEqual(self.result3, ('aehlstx', 2), msg='Incorrect output')