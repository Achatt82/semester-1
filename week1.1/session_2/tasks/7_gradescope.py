# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)

def InputValue():
    try:
        val = float(input("Enter Value: "))
    except ValueError:
        print("That is not a number")

    return val

val1 = InputValue()
val2 = InputValue()

# multiply those numbers together

res = val1 * val2

# print out the result

print(f"Result {res}")

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!