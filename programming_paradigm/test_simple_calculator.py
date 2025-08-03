import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Create a calculator instance before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed signs
        self.assertEqual(self.calc.add(-5, 5), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 7), 7)
    
    def test_subtraction(self):
        """Test subtraction operation"""
        # Test positive results
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative results
        self.assertEqual(self.calc.subtract(3, 5), -2)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test identity
        self.assertEqual(self.calc.subtract(5, 0), 5)
    
    def test_multiplication(self):
        """Test multiplication operation"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test commutative property
        self.assertEqual(self.calc.multiply(4, 5), self.calc.multiply(5, 4))
    
    def test_division(self):
        """Test division operation"""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Test fractional result
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test negative division
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_division_precision(self):
        """Test division with floating point precision"""
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result, 0.333333, places=6)

if __name__ == '__main__':
    unittest.main()