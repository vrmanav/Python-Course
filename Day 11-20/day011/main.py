# DAY 011: Blackjack Capstone

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
from os import system
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "\nYou went over. You lose 😤"
    if user_score == computer_score:
        return "\nIt's a Draw"
    elif computer_score == 0:
        return "\nYou lose, opponent has Blackjack"
    elif user_score == 0:
        return "\nYou win with a Blackjack !!"
    elif user_score > 21:
        return "\nYou went over. You lose."
    elif computer_score > 21:
        return "\nOpponent went over. You win !!"
    elif user_score > computer_score:
        return "\nYou win !!"
    else:
        return "You lose."


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "\nType 'y' to get another card, type 'n' to pass: "
            )
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"\n\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\n\tComputer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? [Y/N] : ") == "y":
    system("clear")
    play_game()
