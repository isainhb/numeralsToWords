numbers_map = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    21: "twenty one",
    22: "twenty two",
    23: "twenty three",
    24: "twenty four",
    25: "twenty five",
    26: "twenty six",
    27: "twenty seven",
    28: "twenty eight",
    29: "twenty nine",
    30: "thirty"
}


def validate_input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("The value was given is not a number. Try again.")
            continue
        else:
            return user_input
            break


def validate_hour(hour_number):
    if 1 <= hour_number <= hour_number:
        return True
    else:
        return False


def validate_minute(minute_number):
    if 0 <= minute_number < 60:
        return True
    else:
        return False


def next_hour(hour):
    next_hour = hour + 1
    if next_hour > 12:
        next_hour = 1
    return next_hour


def time_numerals_to_words(hour, minute):
    str_time = ""
    word_min = ""
    word_hour = numbers_map.get(hour, "!")

    if minute == 0:
        str_time = f"{word_hour} o'clock"
    elif minute == 15:
        str_time = f"quarter past {word_hour}"
    elif minute == 30:
        str_time = f"half past {word_hour}"
    elif minute == 45:
        nxt_hour = next_hour(hour)
        word_next_hour = numbers_map.get(nxt_hour, "!")
        str_time = f"quarter to {word_next_hour}"
    else:
        if 0 < minute < 30:
            minute_res = minute
            print(f"valor de minuto residuo: {minute_res}")
            word_min = numbers_map.get(minute_res)
            str_time = word_min + " past " + word_hour
        elif 30 < minute < 60:
            print(f"Minute: {minute}")
            minute_to_next_hour = 60 - minute
            minute_res = minute_to_next_hour
            word_min = f"{numbers_map.get(minute_res)}"
            nxt_hour = next_hour(hour)
            word_next_hour = numbers_map.get(nxt_hour, "!")
            str_time = word_min + " to " + word_next_hour
    str_time.lower()
    return str_time
