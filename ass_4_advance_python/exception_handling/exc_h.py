# -------------- Exception Handling --------------
# Exception Handling in Python means dealing with errors in a smart way so that your program doesn’t crash.

# ______________ What is an Exception? _____________
# An exception is an error that happens while your program is running.
# Example: dividing by 0, opening a missing file, wrong input, etc.

# ______________ Why use Exception Handling? ______________
# To catch the error and show a message or take another action instead of crashing the program.


try:                                      # Runs the code inside. If there’s an error, it goes to except.
    num = int(input("Enter a number: "))
    print(10 / num)
except:                                   # Runs only if there’s an error in try. Shows an error message.  
    print("Something went wrong!")
else:                                     # Runs only if no error occurs in try. This part is optional.
    print("No error occured")
finally:                                  # Always runs, whether there’s an error or not. Used for cleanup or final message.
    print("Thank you for using the program.")







