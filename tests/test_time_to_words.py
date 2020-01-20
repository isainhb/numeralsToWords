import unittest

from numerals_to_words import time_numerals_to_words


class TimeToWordsValidator(unittest.TestCase):
    def test_zero_minute(self):
        hour = 8
        minute = 0
        self.assertEqual(time_numerals_to_words(hour, minute), "eight o'clock")

    def test_quarter_past(self):
        hour = 3
        minute = 15
        self.assertEqual(time_numerals_to_words(hour, minute), "quarter past three")

    def test_quarter_to(self):
        hour = 5
        minute = 45
        self.assertEqual(time_numerals_to_words(hour, minute), "quarter to six")

    def test_half_hour(self):
        hour = 9
        minute = 30
        self.assertEqual(time_numerals_to_words(hour, minute), "half past nine")

    def test_hour_past(self):
        hour = 7
        minute = 28
        self.assertEqual(time_numerals_to_words(hour, minute), "twenty eight past seven")

    def test_hour_to(self):
        hour = 12
        minute = 55
        self.assertEqual(time_numerals_to_words(hour, minute), "five to one")



