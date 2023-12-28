# Day 005: Password generator

# * Average student heights
# student_heights = input().split()
# for i in range(0, len(student_heights)):
#     student_heights[i] = int(student_heights[i])
# sum = 0
# for i in student_heights:
#     sum += i
# avg = sum / len(student_heights)
# print(f"Average student height is: {avg}")

# * Students' high score
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"Highest score in the class is: {highest_score}")

# * Password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
letters_count = int(input("How many letters would you like in your password?\n")) 
symbols_count = int(input(f"How many symbols would you like?\n"))
numbers_count = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, letters_count + 1):
  password_list.append(random.choice(letters))

for char in range(1, symbols_count + 1):
  password_list += random.choice(symbols)

for char in range(1, numbers_count + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""
for char in password_list:
  password += char

print(f"Generated password is: {password}")