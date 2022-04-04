from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion.word_completer import WordCompleter
import sys
from calculation import Basic
from rich import print

CALC_COMPLETER = WordCompleter(
    ["help", "add(", "sub(", "mul(", "div(", "ans", "quit"], ignore_case=True
)

AVAILABLE_COMMANDS = ["help", "ans", "add", "sub", "mul", "div", "quit"]


class InvalidCommand(Exception):
    pass


class NotANumber(Exception):
    pass


def process_input(user_string, previous):
    """Get the command and numbers is any.

    :param user_string: Input from the user.
    :type user_string: str
    :param previous: Previous answer.
    :type previous: float or int
    :raises NotANumber: Numbers must be integers, floats.
    :return: Command and number(s).
    :rtype: string, int or float
    """

    answer = user_string.replace("(", ",").replace(")", "").split(",")

    command = answer[0]
    if command == "ans":
        numbers = ["ans"]
    else:
        numbers = list()
    for num in answer[1:]:
        try:
            if num == "ans":
                numbers.append(previous)
            else:
                numbers.append(float(num))
        except Exception as err:
            raise NotANumber(f"{num} is not a number. {err}")

    return command, numbers


def main():
    """Run CLI.

    :raises InvalidCommand: Only valid commands will be accepted.
    """
    print("Welcome to the calculator program.")
    print("Type 'help' for a list of functions.")
    b = Basic()
    ans = 0
    while True:
        answer = prompt(
            "Calc> ",
            history=FileHistory("history.txt"),
            auto_suggest=AutoSuggestFromHistory(),
            completer=CALC_COMPLETER,
        )
        try:
            command, numbers = process_input(answer, ans)
            if command not in AVAILABLE_COMMANDS:
                raise InvalidCommand(f"{command} is not a valid command.")
            if command == "quit":
                print("Good bye!")
                sys.exit()
            elif command == "help":
                print("This program can do some basic math.")
                print("help: To display help.")
                print("quit: To exit the program.")
                print("ans: The previous result. Can also be used in a function.")
                print("add(): To add two or more numbers. add(1,2) = 3")
                print("sub(): To subtract two or more numbers. sub(2,1) = 1")
                print("mul(): To multiple two or more numbers. mul(3,4) = 12")
                print("div(): To divide two or more numbers. div(8,2) = 4")
            elif command == "add":
                ans = b.add(*numbers)
            elif command == "sub":
                ans = b.sub(*numbers)
            elif command == "mul":
                ans = b.mul(*numbers)
            elif command == "div":
                ans = b.div(*numbers)

            if command != "help":
                print(f"Answer: {ans}")

        except Exception as err:
            print(err)
