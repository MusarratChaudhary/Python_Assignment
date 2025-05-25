# _________ STUDENT GRADE MANAGER ____________

# Student class represent karta hai ek student ka data aur uska grade logic
class Student:
    def __init__(self, name, marks):
        self.name = name          # Student ka naam store karna
        self.marks = marks        # Student ke marks store karna

    # Grade calculate karne ka method based on marks
    def calculate_grade(self):
        if self.marks >= 90:
            return 'A+'
        elif self.marks >= 80:
            return 'A'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'F'

    # Student ka info print karne ka method (naam, marks, grade)
    def display_info(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name}, Marks: {self.marks}, Grade: {grade}")


# GradeManager class multiple students ko manage karega (add aur show karne ke liye)
class GradeManager:
    def __init__(self):
        self.students = []  # Sab students ko ek list me store karenge

    # Naya student add karne ka method
    def add_student(self, name, marks):
        student = Student(name, marks)
        self.students.append(student)

    # Sab students ka data dikhane ka method
    def show_all_students(self):
        if not self.students:
            print("No student records found.")  # Agar list khali hai
        else:
            print("\nStudent Records:\n")
            for student in self.students:
                student.display_info()


# Yahan se actual program start hota hai
def main():
    gm = GradeManager()  # GradeManager class ka object banaya

    while True:
        print("\n=== Student Grade Manager ===")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            try:
                marks = float(input("Enter student marks (out of 100): "))
                gm.add_student(name, marks)  # Add student to list
                print("Student added successfully!")
            except ValueError:
                print("Please enter valid numeric marks.")
        elif choice == "2":
            gm.show_all_students()  # Show all students info
        elif choice == "3":
            print("Exiting program. Goodbye!")  # Exit message
            break
        else:
            print("Invalid choice. Please select again.")  # Invalid input

# Is line ka matlab: agar file directly run ho rahi hai to main() run karo
if __name__ == "__main__":
    main()
