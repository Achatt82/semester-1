# Fill out the code to make a very simple calculator

def getInput():
    while True:
        try:
            val = float(input("Enter value:"))
            break
        except ValueError:
            print("Invalid value")

    return val

# ask the user to enter number1:

num1 = getInput()

# ask the user to enter number 2:

num2 = getInput()

# calculate the result of adding those numbers together

res = num1 + num2

# print out the answer

print(f"Result: {res}")