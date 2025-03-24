# --------------------------------------
# ------------CONTROL FLOW--------------
# --------------------------------------
# Python programs execute line by line, but sometimes, you need to control the flow of execution 
# based on conditions or repeat certain tasks. This is done using Control Flow and Loops.

# ----------------------------------------
# 1) CONDITIONAL STATEMENTS (If-Elif-Else) -> Used for decision-making.
# ----------------------------------------

# if -> To executes a block of code only if the first condition is True.
# elif -> To checks multiple additional conditions. It stands for "else if."
# else -> When none of the conditions are true.

num = 10

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# ----------------------------------------
# 2) COMPARISON & LOGICAL OPERATORS IN CONDITIONAL STATEMENTS:
# ----------------------------------------
# Comparison Operators (==, >, <, >=, <=) compare values.
# These operators are used in if-elif-else conditions to make decisions.

a = 10
b = 20

if a < b:  # This condition checks if 'a' is smaller than 'b'
    print("a is smaller than b")

# Logical Operators (and, or, not) -> Used to check multiple conditions at the same time.

#  AND -> Returns True only if both conditions are True.
x = 5
y = 15

if x > 0 and y > 10:  # Both conditions must be True
    print("Both conditions are true")

#  OR -> Returns True if at least one condition is True.
if x > 0 or y < 10:  # If either condition is True, it runs.
    print("At least one condition is true")

#  NOT -> Reverses the condition (True -> False, False -> True)
if not x < 0:  # If x is NOT less than 0, it runs.
    print("x is not negative")
