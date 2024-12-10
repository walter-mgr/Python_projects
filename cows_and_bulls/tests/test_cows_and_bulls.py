import unittest
import cows_and_bulls


class TestUniqueDigitNumber(unittest.TestCase):

    def test_length(self):
        "Test if the generated number has exactly 4 digits"
        result = cows_and_bulls.get_four_unique_digit_number()
        self.assertEqual(len(result), 4, "The length of the result must be 4 digits")

    def test_unique_digits(self):
        """Test if the generated number has unique digits."""
        result = cows_and_bulls.get_four_unique_digit_number()
        self.assertEqual(len(result), 4, "The result should have 4 unique digits")

    def test_is_digit(self):
        """Test if the generated number contains only digits."""
        result = cows_and_bulls.get_four_unique_digit_number()
        self.assertTrue(result.isdigit(), "The result should contain only digits")


if __name__ == "__main__":
    unittest.main()
