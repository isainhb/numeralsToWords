class TimeNumeralsToWords:
    NUMBERS_TEXT = {
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
        30: "thirty",
    }

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.words = ""

    def time_numerals_to_words(self):
        str_time = ""
        word_hour = self.NUMBERS_TEXT.get(self.hour, "!")

        if self.minute == 0:
            str_time = f"{word_hour} o'clock"
        elif self.minute == 15:
            str_time = f"quarter past {word_hour}"
        elif self.minute == 30:
            str_time = f"half past {word_hour}"
        elif self.minute == 45:
            nxt_hour = TimeNumeralsToWords.next_hour(self.hour)
            word_next_hour = self.NUMBERS_TEXT.get(nxt_hour, "!")
            str_time = f"quarter to {word_next_hour}"
        else:
            if 0 < self.minute < 30:
                minute_res = self.minute
                word_min = self.NUMBERS_TEXT.get(minute_res)
                str_time = word_min + " past " + word_hour
            elif 30 < self.minute < 60:
                minute_to_next_hour = 60 - self.minute
                minute_res = minute_to_next_hour
                word_min = f"{self.NUMBERS_TEXT.get(minute_res)}"
                nxt_hour = TimeNumeralsToWords.next_hour(self.hour)
                word_next_hour = self.NUMBERS_TEXT.get(nxt_hour, "!")
                str_time = word_min + " to " + word_next_hour
        str_time.lower()
        self.words = str_time

    def to_string(self):
        return self.words

    @staticmethod
    def next_hour(hour_num):
        next_hour = hour_num + 1
        if next_hour > 12:
            next_hour = 1
        return next_hour
