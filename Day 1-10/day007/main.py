# Day 007: Hangman Game

from random import choice
from os import system
from time import sleep
from art import stages, logo

word_list = [
    "overwhelm",
    "profound",
    "family",
    "opposite",
    "crown",
    "routine",
    "constitution",
    "friendly",
    "smooth",
    "knot",
]
lives = 6
game_over = False

#! T0: Pick random word from the word list
chosen_word = choice(word_list)
word_len = len(chosen_word)

#! T1: Make equivalent no. of blanks & show it to user
answer = []
for char in range(0, word_len):
    answer.append(" _ ")
print(logo)
print(f"{' '.join(answer)}")
while not game_over:
    #! T6: Show user the status of the hangman
    print(stages[lives])

    #! T2: Ask user to make a guess
    user_guess = input("Make your guess: ").lower()

    #! T7: Check if your has typed an alredy correct guessed alphabet
    if user_guess in answer:
        print("⚠️ You've already guessed the alphabet")
        sleep(1.5)

    #! T3: Check if the user has made the correct guess
    for position in range(0, word_len):
        if user_guess == chosen_word[position]:
            answer[position] = user_guess

    #! T4: Check if user lost all the lives
    if user_guess not in chosen_word:
        print("🚨 INCORRECT! You've made a wrong guess. You lose a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print("Better luck next time !!")
        sleep(1.5)

    #! T5: Check if user guessed the entire word
    if " _ " not in answer:
        game_over = True
        print("🎉 You WIN !! 🎉")
        sleep(3)
    sleep(0.5)
    system("clear")
    print(f"{' '.join(answer)}")
