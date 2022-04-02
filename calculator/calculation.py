"""
Calculator Functions
--------------------

Various calculator functions.
"""


class DivideByZero(Exception):
    pass


class NotEnoughNumbers(Exception):
    pass


class Basic:
    """Basic calculations."""

    def __init__(self):
        self.previous_result: float = 0

    def add(self, *args):
        total = 0
        count = 0
        for number in args:
            total += number
            count += 1

        if count < 2:
            raise NotEnoughNumbers(f"Only one number was given: {total}")
        return total

    def sub(self, *args):
        total = 0
        count = 0
        for number in args:
            if total == 0:
                total += number
            else:
                total -= number
            count += 1

        if count < 2:
            raise NotEnoughNumbers(f"Only one number was given: {total}")

        return total

    def mul(self, *args):
        total = 0
        count = 0
        for number in args:
            if total == 0:
                total += number
            else:
                total *= number
            count += 1

        if count < 2:
            raise NotEnoughNumbers(f"Only one number was given: {total}")

        return total

    def div(self, *args):
        total = 0
        count = 0
        for number in args:
            if total == 0:
                total += number
            else:
                if number == 0:
                    raise DivideByZero("Can't divide by zero.")
                total /= number
            count += 1

        if count < 2:
            raise NotEnoughNumbers(f"Only one number was given: {total}")

        return total
