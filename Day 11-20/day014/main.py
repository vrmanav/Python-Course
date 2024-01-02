# Day 014: Higher or Lower game

from logo import logo, vs
from game_data import data
from random import choice
from os import system
from time import sleep


def get_random_account():
    return choice(data)


def format_data(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"


def check_guess(guess, acc_a, acc_b):
    acc_a_follower = acc_a["follower_count"]
    acc_b_follower = acc_b["follower_count"]
    if acc_a_follower > acc_b_follower:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    continue_game = True
    print(logo)
    acc_a = get_random_account()
    acc_b = get_random_account()
    while continue_game:
        acc_a = acc_b
        while acc_a == acc_b:
            acc_b = get_random_account()
        print(f"Compare A: {format_data(acc_a)}")
        print(vs)
        print(f"Compare B: {format_data(acc_b)}")
        guess = input("Who do you think has more followers? [A/B]:\n").lower()
        is_correct = check_guess(guess, acc_a, acc_b)

        if is_correct:
            score += 1
            print(f"✅ You're right! Current score: {score}")
            sleep(2)
            system("clear")
        else:
            continue_game = False
            print(f"❌ Sorry, that's wrong. Final score: {score}")
            sleep(2)


game()
