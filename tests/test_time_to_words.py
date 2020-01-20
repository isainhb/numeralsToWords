import unittest

from utils.numerals_to_words import TimeNumeralsToWords
from utils.validate import ValidateTime


class TimeToWordsValidator(unittest.TestCase):
    def test_zero_minute(self):
        hour = 8
        minute = 0
        time_numeral_words = TimeNumeralsToWords(hour, minute)
        time_numeral_words.time_numerals_to_words()
        self.assertEqual(time_numeral_words.to_string(), "eight o'clock")

    def test_quarter_past(self):
        hour = 3
        minute = 15
        time_numeral_words = TimeNumeralsToWords(hour, minute)
        time_numeral_words.time_numerals_to_words()
        self.assertEqual(time_numeral_words.to_string(), "quarter past three")

    def test_quarter_to(self):
        hour = 5
        minute = 45
        time_numeral_words = TimeNumeralsToWords(hour, minute)
        time_numeral_words.time_numerals_to_words()
        self.assertEqual(time_numeral_words.to_string(), "quarter to six")

    def test_half_hour(self):
        hour = 9
        minute = 30
        time_numeral_words = TimeNumeralsToWords(hour, minute)
        time_numeral_words.time_numerals_to_words()
        self.assertEqual(time_numeral_words.to_string(), "half past nine")

    def test_hour_past(self):
        hour = 7
        minute = 28
        time_numeral_words = TimeNumeralsToWords(hour, minute)
        time_numeral_words.time_numerals_to_words()
        self.assertEqual(time_numeral_words.to_string(), "twenty eight past seven")

    def test_hour_to(self):
        hour = 12
        minute = 55
        time_numeral_words = TimeNumeralsToWords(hour, minute)
        time_numeral_words.time_numerals_to_words()
        self.assertEqual(time_numeral_words.to_string(), "five to one")

    def test_validation_hour(self):
        validate = ValidateTime()

        # These values are string due to we are simulating the values given by input
        valid_hour = validate.validate_hour("5")
        invalid_hour_value = validate.validate_hour('test')
        invalid_hour_range = validate.validate_hour("25")

        self.assertTrue(valid_hour)
        self.assertFalse(invalid_hour_value)
        self.assertFalse(invalid_hour_range)

    def test_validation_minute(self):
        validate = ValidateTime()

        # These values are string due to we are simulating the values given by input
        valid_min = validate.validate_minute("35")
        invalid_min_value = validate.validate_hour('test minute')
        invalid_min_range = validate.validate_hour("70")

        self.assertTrue(valid_min)
        self.assertFalse(invalid_min_value)
        self.assertFalse(invalid_min_range)

