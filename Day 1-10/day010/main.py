# Day 010: Calculator app
from art import logo
from os import system


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


print(logo)


def calculator():
    n1 = float(input("Enter the first number:\n"))
    do_continue = True
    while do_continue:
        for symbol in operations:
            print(f"{symbol}  ", end="")
        operation_symbol = input(
            "\nEnter the symbol whose operation you would like to perform?\n"
        )
        n2 = float(input("Enter the next number:\n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if (
            input(
                f"\nType Y to continue with {answer} or type NEW to start a new calculation:\n"
            ).lower()
            == "new"
        ):
            do_continue = False
            system("clear")
            calculator()
        else:
            n1 = answer


calculator()
