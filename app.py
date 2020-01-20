from utils.validate import input_hour, input_minute
from utils.numerals_to_words import TimeNumeralsToWords

hour = input_hour()
minute = input_minute()
word_transform = TimeNumeralsToWords(hour, minute)
word_transform.time_numerals_to_words()
print(word_transform.to_string())
