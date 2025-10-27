class ValidateTime:
    ERROR_MSGS = {
        "not_number": "The value was given is not a number. Try again.",
        "hour_range": "The value was given only can be a number between 1 and 12.",
        "minute_range": "The value was given only can be a number between 0 and 59.",
    }

    @staticmethod
    def validate_hour(hour_str):
        if not hour_str.isnumeric():
            print("The value was given is not a number. Try again.")
            return False

        hour = int(hour_str)
        if not ValidateTime.validate_numeric_range(hour, 1, 12):
            print("The value was given only can be a number between 1 and 12.")
            return False
        return True

    @staticmethod
    def validate_minute(minute_str):
        if not minute_str.isnumeric():
            print("The value was given is not a number. Try again.")
            return False
        minute = int(minute_str)
        if not ValidateTime.validate_numeric_range(minute, 0, 59):
            print("The value was given only can be a number between 0 and 59.")
            return False
        return True

    @staticmethod
    def validate_numeric_range(number, min_val, max_val):
        return True if min_val <= number <= max_val else False


def input_hour():
    while True:
        hour_str = input("Type hour (1 - 12) ----> ")
        valid = ValidateTime.validate_hour(hour_str)
        if not valid:
            continue
        hour = int(hour_str)
        return hour


def input_minute():
    while True:
        minute_str = input("Type minute (0 to 59) ----> ")
        valid = ValidateTime.validate_minute(minute_str)
        if not valid:
            continue
        minute = int(minute_str)
        return minute
