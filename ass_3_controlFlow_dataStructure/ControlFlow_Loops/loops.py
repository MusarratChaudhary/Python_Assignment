# ----------------------------------------
# 1) ITERATION STATEMENTS/LOOPS (for, while) -> Used to repeat code.
# ----------------------------------------

# FOR LOOP -> Runs a block of code multiple times.
for i in range(3):
    print("Hello World!:", i)  # This loop will run from 0 to 2 and print three times.

# WHILE LOOP -> Runs as long as the condition is True.
count = 1
while count <= 3:
    print("Count:", count)  # The loop will run as long as count <= 3
    count += 1

# ----------------------------------------
# 2) NESTED LOOPS (Loop inside another loop)
# ----------------------------------------
# Sometimes, we need to use one loop inside another loop. 
# This is called a **Nested Loop**, and it is useful for working with tables, matrices, and patterns.

fruits = ["apple", "banana", "mango"]

if "apple" in fruits:  # Outer if
    print("Apple is in the list")
    
    if "cherry" in fruits:  # Inner if
        print("Cherry is in the list")
    else:
        print("Cherry is not in the list")  # This will execute because cherry is not in the list
        

# ----------------------------------------
# 3) TRANSFER STATEMENTS (break, continue, pass) -> Used to control loop flow.
# ----------------------------------------

# BREAK -> Stops the loop when a condition is met.
for i in range(5):
    if i == 3:
        break  # The loop will stop at 3 and will not continue further.
    print(i)

# CONTINUE -> Skips the current iteration and moves to the next.
for i in range(5):
    if i == 2:
        continue  # It will skip 2, and the remaining numbers will be printed.
    print(i)

# PASS -> Used as a placeholder when code is not yet written.
for i in range(5):
    if i == 2: 
        pass  # Pass means "do nothing," but it will not cause an error.
    print(i)