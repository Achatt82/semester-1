# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

# Prints the user_string variable on a new line.
print(f"\nOriginal String: {user_string}")

# Prints the user_string variable in all lowercase.
print(f"Modified String 1: {user_string.lower()}")

# Prints the user_string variable in all uppercase.
print(f"Modified String 2: {user_string.upper()}")

# Removes any trailing or leading whitespace characters.
print(f"Modified String 3: {user_string.strip()}")

# Replaces any instance of the letter 'a' in user_string with the symbol '@'.
print(f"Modified String 4: {user_string.replace('a', '@')}")

# Makes the first character of the string capitalised, and any remaining characters lowercase.
print(f"Modified String 5: {user_string.capitalize()}")

# Returns the string in reverse order.
print(f"Modified String 6: {user_string[::-1]}")

# Capitalises every first letter of a word in a sentence.
print(f"Modified String 7: {user_string.title()}")

# Returns the number of characters in a string (its length).
print(f"Modified String 8: {len(user_string)}")

# Returns the index (location) of the first instance of the letter 'a' in the string.
print(f"Modified String 9: {user_string.find('a')}")

# Returns how many instances of the letter 'a' are in the string.
print(f"Modified String 10: {user_string.count('a')}")

# Returns a boolean value with the condition if the string starts with 'Hello'.
print(f"Modified String 11: {user_string.startswith('Hello')}")

# Returns a boolean value with the condition if the string ends with the character '!'.
print(f"Modified String 12: {user_string.endswith('!')}")

# Checks if the string only containts alpha-numeric characters, returns a boolean.
print(f"Modified String 13: {user_string.isalnum()}")

# Checks if the string only contains letters, returns a boolean.
print(f"Modified String 14: {user_string.isalpha()}")

# Checks if the string only contains numbers. returns a boolean.
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!