import unittest
from mymodule import square, double

class TestMyModule(unittest Testcase):
  def test_square(self):
    self.assertEqual(square(2),4)
    self.assertEqual(square(3.0),9.0)
    self.assertEqual(square(-3),-9)
  def test_double(self):
    self.assertEqual(double(3),6)
    self.assertEqual(double(2),4)
    self.assertEqual(double(-3.1),-6.2)
    self.assertEqual(double(0),0)
def test_add(self):
      self.assertEqual(add(3,2), 5)
      self.assertEqual(add(3.6,2.3), 5.9)
      self.assertNotEqual(add("hello"," world"), "helloworld")
if __name__ == "__main__":
  unittest.main()
  
