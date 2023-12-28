# DAY 009: Secret Auction
from os import system

end_of_auction = False
bid_dict = {}


def find_highest_bidder(bid_dict):
    print()
    highest_bid = 0
    winner = ""
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            winner = bidder
            highest_bid = bid_amount
    print(f"{winner} WINS !! with the bid amount of ₹{bid_amount}")


while not end_of_auction:
    # !T0: Ask user's name
    user_name = input("What is your name?\n")

    # !T1: Ask for bidding price
    bid_amount = int(input("How much amount do you want to bid?\n₹"))

    # !T2: Add the new user's details to dictionary
    bid_dict[user_name] = bid_amount

    # !T3: Ask is there any new user
    new_user = input("Is there any other user who wants to bid? [Y/N]\n").lower()
    if new_user == "n":
        end_of_auction = True
        find_highest_bidder(bid_dict)
    elif new_user == "y":
        system("clear")
