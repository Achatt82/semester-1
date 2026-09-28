"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Alex Chatterton
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

while True:
    try:
        monthly_savings = int(input("Enter your monthly savings amount: "))
        break
    except ValueError:
        print ("Invalid amount.")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

annum = monthly_savings * 12
print(f"You will save {annum} per year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

annum += (annum * 0.008)
print(f"With interest, you will save £{annum:.2f} per year.")