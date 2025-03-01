# PYTHON KEYWORDS
# Keywords are reserved words in Python that have special meanings and cannot be used as variable names.
# Here is a list of the Python keywords.There are 35 keywords

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not      

# Getting List of all Python keywords:
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)


# Some common Python keywords:

# Operator Keywords: and, or, not, in, is
# 1. and
# Used for a logical operator & condition
x = 5
y = 10
if x > 0 and y > 5:
    print("Both conditions are True")

# 2. or
# Used for logical operator OR condition
if x > 0 or y < 5:
    print("At least one condition is True")

# 3. not
# Used to reverse the boolean result
is_active = False
print(not is_active)  

# 4. in
# Check if an element exists in a sequence
numbers = [1, 2, 3, 4]
print(2 in numbers)  # True (2 list me hai)
print(5 in numbers)  # False (5 list me nahi hai)

# 5. is
# Check if two variables are identical then return True
print(2 is 2)

# Conditional keywords in Python: if, else, elif
# 6. if
# Used for conditional statements
age = 20
if age > 18:
    print("You are an adult")

# 7. elif
# Used for multiple conditions
if age > 30:
    print("Old")
elif age > 18:
    print("Adult")

# 8. else
# Used for default condition
if age > 30:
    print("Old")
else:
    print("Not old")

# Iteration Keywords: for, while, break, continue, pass
# 9. for
# Used for loops
for i in range(5):
    print(i)

# 10. while
# Used for loops with condition
count = 0
while count < 3:
    print(count)
    count += 1

# 11. break
# Used to stop the loop
for i in range(5):
    if i == 3:
        break
    print(i)

# 12. continue
# Used to skip the current iteration
for i in range(5):
    if i == 3:
        continue
    print(i)

# 13. pass
# Used as a placeholder
def my_function():
    pass  # Nothing happens here

# Structure Keywords : def, class, return, lambda
# 14. def
# Defines a function using the def keyword.
def greet():
    print("Hello, World!")
greet()

# 15. class
# Create a class
class Person:       # class creat a blueprint
  name = "John"
  age = 36
# Create an object named p1
p1 = Person()
print(p1.name)      # object performs the work


# 16. return
# Used to return value from a function
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# 17. lambda
# Create a one-line anonymous function
sum = lambda a, b: a + b
print(sum(5, 3))


