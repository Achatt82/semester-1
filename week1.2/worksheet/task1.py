# Worksheet 1.2: Task 1 Solution
import sys

try:
    value = int(input("Please enter a grade (0 - 100): "))
except ValueError:
    # sys.exit() not needed here because the program will exit after throwing an exception.
    print("Error: Grade must be an integer between 0 and 100")

if (not (0 <= value <= 100)):
    sys.exit("Error: Grade must be an integer between 0 and 100")

match value:
    case _ if (0 <= value <= 39):
        grade = "Fail"
    case _ if (40 <= value <= 69):
        grade = "Pass"
    case _ if (70 <= value <= 100):
        grade = "Distinction"

print(f"The students grade is: {grade}.")