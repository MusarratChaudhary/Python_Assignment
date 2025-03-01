# INTRODUCTION TO PYTHON
# Python is a high-level programming language. It was created by Guido van Rossum and released in 1991.
# Python is mainly used for backend development. It is simple, powerful, and versatile.
# Python has easy-to-read syntax and works for various applications.

# DATA TYPES
# Data types specify the type of value a variable holds. Python has several built-in data types.
# Python data types are categorized into two types:
# 1- Mutable Data Type – Values can be changed.
# 2- Immutable Data Type – Values cannot be changed.

# PRIMARY DATA TYPES CATEGORIES
# 1- Numeric Data Types (Immutable): integer, float, complex
# 2- Sequence Data Types: list (mutable), tuple (immutable), range
# 3- Set Data Types: set (mutable), frozenset (immutable)
# 4- Mapping Data Types: dictionary (mutable)
# 5- String Data Types (Immutable)
# 6- Boolean Data Types (Immutable)
# 7- None Data Types

# MOST COMMONLY USED DATA TYPES

# 1- String (str) – Textual data with quotation marks
id_card: str = "Musarrat"
print(id_card)

# Triple quotes allow multi-line strings
id_card: str = """Name: Musarrat
Father Name: Musharaf
Age: 22"""
print(id_card)

# 2- Integer (int) – Whole numbers
num: int = 35
print(type(num))  # Shows the data type
print(num)

# 3- Float (float) – Decimal numbers
float_num: float = 3.5
print(type(float_num))
print(float_num)

# 4- Boolean (bool) – True or False values
is_true: bool = True
is_false: bool = False
print(type(is_true))
print(is_true)

# 5- List (list) – Ordered, changeable collection
fruits: list[str] = ["Apple", "Mango", "Banana"]
print(type(fruits))
print(fruits)
print(fruits[0])  # First element
print(fruits[-1])  # Last element
fruits[1] = "Orange"  # Changing value
print(fruits)

# 6- Tuple (tuple) – Ordered, unchangeable collection
vegetables: tuple = ("Tomato", "Potato", "Chilli")
print(type(vegetables))
print(vegetables)
# vegetables[1] = "Brinjal"  # This will give an error

# 7- Dictionary (dict) – Key-value pairs
user_data: dict[str, str] = {
    "Name": "Musarrat",
    "Father_Name": "Musharaf"
}
print(type(user_data))
print(user_data)

# 8- Set (set) – Unordered collection of unique items
fruits = {"Apple", "Apple", "Mango", "Banana"}  # Duplicate ignored
print(fruits)
fruits.add("Orange")
fruits.remove("Banana")
print(fruits)

# 9- Frozen Set (frozenset) – Unordered, unchangeable collection
numbers = frozenset([1, 2, 3, 4, 2, 1])
print(numbers)
# numbers.add(5)  # This will give an error

# 10- None – Represents absence of value
x = None
print(x)
print(type(x))



