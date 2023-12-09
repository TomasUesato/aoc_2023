import unittest
from day_01 import first_digit, last_digit


class TestStringMethods(unittest.TestCase):

    def test_first_digit_beginning(self):
        input = "2aonthg"
        expected = "2"
        self.assertEquals(first_digit(input), expected)

    def test_first_digit_middle(self):
        input = "aon2thg"
        expected = "2"
        self.assertEquals(first_digit(input), expected)

    def test_last_digit_end(self):
        input = "aon2three5"
        expected = "5"
        self.assertEquals(last_digit(input), expected)

    def test_last_digit_middle(self):
        input = "aon2te5ae"
        expected = "5"
        self.assertEquals(last_digit(input), expected)

    def test_first_digit_with_only_one(self):
        input = "aon2teae"
        expected = "2"
        self.assertEquals(first_digit(input), expected)

    def test_last_digit_with_only_one(self):
        input = "aon2teae"
        expected = "2"
        self.assertEquals(last_digit(input), expected)

    def test_first_digit_spelled(self):
        input = "aone2three"
        expected = "1"
        self.assertEquals(first_digit(input), expected)

    def test_last_digit_spelled(self):
        input = "aone2three"
        expected = "3"
        self.assertEquals(last_digit(input), expected)


if __name__ == '__main__':
    unittest.main()
