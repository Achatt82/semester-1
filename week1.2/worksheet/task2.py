# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers
#
values = read_numbers()

# Edge cases
if len(values) == 0:
    sys.exit("Error: no numbers provided")

minimum = min(values)
maximum = max(values)
mean = sum(values) / len(values)

values = sorted(values)
middle = len(values) // 2

if (len(values) % 2 == 0 ):
    median = (values[middle - 1] + values[middle]) / 2
else:
    median = values[middle]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")
