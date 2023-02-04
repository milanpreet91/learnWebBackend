import unittest
from mymodule import square, double

class TestMyModule(unittest Testcase):
  def test_square(self):
    self.assertEqual(square(2),4)
  def test_double(self):
    self.assertEqual(double(3),6)

if __name__ == "__main__":
  unittest.main()
  
