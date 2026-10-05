# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)

# I think this will print the items that appear in both arrays (A n B)

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food)

# It displays 5 Items because it displays any unique items that exist within either array (A U B)

# Add an item to fruit

fruit.add("banana")
print(fruit)

# Remove an item from vegetables
fruit.pop()
print (fruit)

# Find and display symmetric difference of the two sets
sym_dif = food - both
print (sym_dif)