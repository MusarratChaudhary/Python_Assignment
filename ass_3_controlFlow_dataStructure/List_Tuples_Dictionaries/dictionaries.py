# ----------------------------------
# ------------DICTIONARY------------
# ----------------------------------

# A dictionary is a collection of key-value pairs. It is:
# Ordered (since Python 3.7): Items are stored in the order they were inserted.
# Mutable: Items can be added, removed, or modified after the dictionary is created.
# Un-indexed: Items are accessed using keys, not indices.
# Without duplicates: Keys must be unique, but values can be duplicated.

# Create dictionary
person = {
    "name": "Ali",
    "age": 25,
    "city": "Karachi"
}
print(person)

print(len(person))

# Get all items (key + value)
print(person.items())

# Get all keys
print(person.keys())

# Get all values
print(person.values())

# Loop through dictionary
for key, value in person.items():     # To print each key-value pair in a specific style or format.
    print(key, ":", value)

# Check if a key exists
print("name" in person)              # Output: True (because "name" key is present in the dictionary)

# Access value by key
print(person["name"])                # Output: Ali

# Add new item
person["email"] = "ali@gmail.com"
print("After Adding Email:", person)

# Update value
person["age"] = 26
print("After Updating Age:", person)

# Remove item
person.pop("city")
print("After Removing City:", person)


# Copy dictionary
person_data = person.copy()
print("Copy:", person_data)

# Clear dictionary
person.clear()
print("After Clear:", person)    # Output: {}
