import unittest

class MySortTestCases(unittest.TestCase):
  def setUp(self):
    self.result1 = my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    self.result2 = my_sort([1, 2])
    self.result3 = my_sort([2, 1])
    self.result4 = my_sort([3, 3, 4])
    self.result5 = my_sort([90, 45, 66])

  def test_output_1(self):
    self.assertEqual(self.result1,  [1, 3, 5, 7, 9, 2, 4, 6, 8, 10], msg='Invalid sorted output')
    
  def test_output_2(self):
    self.assertEqual(self.result2,  [1, 2], msg='Invalid sorted output')
    
  def test_output_3(self):
    self.assertEqual(self.result3,  [1, 2], msg='Invalid sorted output')
  
  def test_output_4(self):
    self.assertEqual(self.result4,  [3, 3, 4], msg='Invalid sorted output')
    
  def test_output_5(self):
    self.assertEqual(self.result5,  [45, 66, 90], msg='Invalid sorted output')