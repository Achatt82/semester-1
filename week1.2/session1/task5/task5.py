# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database

new = rivers.copy()

new["York"] = "Ouse"
new["Manchester"] = "Irwell"
print(new)

# Display all the keys
print(new.keys())

# Display all the values
print(new.values())

# Display all the key:value pairs, as tuples
for key in new.keys():
    print([key, new.get(key)])

# Delete an entry from the rivers database
new.popitem()
print(new)

# Or you can use dict.pop(key) for a specific key-value pair