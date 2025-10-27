# Pytest
import pytest

from utils.numerals_to_words import TimeNumeralsToWords
from utils.validate import ValidateTime


def test_zero_minute():
    hour = 8
    minute = 0
    time_numeral_words = TimeNumeralsToWords(hour, minute)
    time_numeral_words.time_numerals_to_words()
    assert time_numeral_words.to_string() == "eight o'clock"


def test_quarter_past():
    hour = 3
    minute = 15
    time_numeral_words = TimeNumeralsToWords(hour, minute)
    time_numeral_words.time_numerals_to_words()
    assert time_numeral_words.to_string() == "quarter past three"


def test_quarter_to():
    hour = 5
    minute = 45
    time_numeral_words = TimeNumeralsToWords(hour, minute)
    time_numeral_words.time_numerals_to_words()
    assert time_numeral_words.to_string() == "quarter to six"


@pytest.mark.parametrize(
    "hour, minute, expected",
    [
        (9, 30, "half past nine"),
        (7, 28, "twenty eight past seven"),
        (12, 55, "five to one"),
    ],
)
def test_some_time(hour, minute, expected):
    time_numeral_words = TimeNumeralsToWords(hour, minute)
    time_numeral_words.time_numerals_to_words()
    assert time_numeral_words.to_string() == expected
