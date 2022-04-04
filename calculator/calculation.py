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
        """Add multiple numbers.

        :raises NotEnoughNumbers: A minimum of 2 numbers are required.
        :return: Summation of the provided numbers.
        :rtype: int or float
        """
        total = 0
        count = 0
        for number in args:
            total += number
            count += 1

        if count < 2:
            raise NotEnoughNumbers(f"Only one number was given: {total}")
        return total

    def sub(self, *args):
        """Subtract multiple numbers.

        :raises NotEnoughNumbers: A minimum of 2 numbers are required.
        :return: Total after subtracting the provided numbers.
        :rtype: int or float
        """
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
        """Multiple multiple numbers.

        :raises NotEnoughNumbers: A minimum of 2 numbers are required.
        :return: Total after multiplying the provided numbers.
        :rtype: int or float
        """
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
        """Divide multiple numbers.

        :raises DivideByZero: Cannot divide by 0.
        :raises NotEnoughNumbers: A minimum of 2 numbers are required.
        :return: Total after dividing the provided numbers.
        :rtype: int or float
        """
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
