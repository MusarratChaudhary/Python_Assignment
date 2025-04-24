# ------------ File Handling ----------------
# File handling means working with files in Python — like creating, reading, writing, or deleting files. 
# It lets us store data permanently on our computer, so it doesn't get lost when the program ends.

# _____________ Read Mode __________________
# If data.txt file is not exist in folder then it will give an error.
# If data.txt file is exist then it will run.

file = open("data.txt", "r")       # Opens the file named data.txt in read mode ("r"), so we can read its content.
content = file.read()              # Reads all the text inside the file and saves it in the content variable. 
print(content)                     # Prints whatever was inside the file.
file.close()                       # Closes the file to free up memory/resources. Always a good practice!

# ______________ Write Mode ____________________
# In write mode ("w"):
# If the file already exists, its old content is deleted and new data is added.
# If the file doesn't exist, a new file is created with the given name and new data is added in new file.

file = open("data.txt", "w")              
file.write("Hello, this is Musarrat!\n")        # This line writes the text into the file and move on next line.
file.write("This is write mode :)")
file.close()

# _______________ Append Mode _____________________
# In append mode ("a"):
# If the file exists, new data is added at the end without deleting the old content.
# If the file doesn't exist, a new file is created and data is added to it.
file = open("data.txt", "a")
file.write("\nThis is extra info added later.")
file.close()

# _______________ Exclusive Creation Mode _________________
# Exclusive Creation Mode ("x"):
# If the file already exists, it will give an error.
# If the file doesn't exist, it will create a new file and write data in it.
file = open("new_file.txt", "x")
file.write("This is a newly created file.")
file.close()


# ________________ Use with statement for cleaner code _________________
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
