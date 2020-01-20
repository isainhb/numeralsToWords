import numerals_to_words
from numerals_to_words import time_numerals_to_words

hour = int(input("Type hour (1 - 12) ----> "))
minute = int(input("Type minute (0 to 59) ----> "))
time_words = time_numerals_to_words(hour, minute)

print(time_words)