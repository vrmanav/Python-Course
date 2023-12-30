# Day 012: Number guessing game

#! SCOPE - Local vs. Global
# enemies = 1
# def increase_enemies():
#     enemies = 2
#     Local variable
#     print(f"Enemies inside function {enemies}")
# increase_enemies()
# Global variable
# print(f"Enemies outside function {enemies}")

#! Accessing global variable inside a local scope
# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 4
#     print(f"Enemies inside function {enemies}")
# increase_enemies()
# print(f"Enemies outside function {enemies}")

from random import randint

attempts = 0
generated_no = randint(1, 101)


def set_attempts(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5


def check_guess(user_guess, attempts):
    if user_guess > generated_no:
        print("\nToo High")
        return attempts - 1
    elif user_guess < generated_no:
        print("\nToo Low")
        return attempts - 1
    elif user_guess == generated_no:
        print("\nCONGRATULATIONS !! You've guessed it.")


print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("\nChoose a difficulty. [EASY/HARD]:\n").lower()
attempts = set_attempts(difficulty)

user_guess = 0
while user_guess != generated_no:
    print(f"\nYou have {attempts} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))

    attempts = check_guess(user_guess, attempts)
    if attempts == 0:
        print("\nYou are out of attempts. YOU LOSE !!")
    elif user_guess != generated_no:
        print("\nGUESS AGAIN")
