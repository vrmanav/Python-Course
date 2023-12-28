# DAY 002: Tip Calculator

print("Welcome to Tip Calculator!")
bill = float(input("What is the total bill? ₹"))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill?"))

percent_tip = tip / 100
total_tip = bill * percent_tip
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_bill = round(bill_per_person, 2)

print(f"Each person should pay: ${final_bill}")