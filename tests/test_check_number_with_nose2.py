import unittest
from src.check_number import check_number

class TestSum(unittest.TestCase):

    def test_check_number(self):
        self.assertEqual(check_number("-22"), "Negative")
        self.assertEqual(check_number("0"), "Zero")
        self.assertEqual(check_number("10"), "Positive")
        
if __name__ == '__main__':
    import nose2
    nose2.main() 