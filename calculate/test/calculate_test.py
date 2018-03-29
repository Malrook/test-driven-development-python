import unittest
import sys
sys.path.insert(0, '/root/Desktop/calculate')
from calculate import *

class TestCalculate(unittest.TestCase):
	def setUp(self):
		self.calc = Calculate()

	def test_add_method_returns_correct_result(self):
		self.assertEqual(4, self.calc.add(2, 2))

	def test_subtract_method_returns_correct_result(self):
		self.assertEqual(3, self.calc.subtract(4,1))

	def test_multiply_method_returns_correct_result(self):
		self.assertEqual(10, self.calc.multiply(5,2))

	def test_divide_method_returns_correct_result(self):
		self.assertEqual(12, self.calc.divide(24,2))




if __name__ == '__main__':
	unittest.main()