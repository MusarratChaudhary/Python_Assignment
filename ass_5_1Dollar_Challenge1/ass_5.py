# ________Student Report Card__________

# Parent class representing a student
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        # Show basic student information
        print(f"\nName: {self.name}")
        print(f"Roll No: {self.roll_no}")

# Child class that inherits from Student
class ReportCard(Student):
    def __init__(self, name, roll_no, subjects):
        # Use parent class constructor
        super().__init__(name, roll_no)
        self.subjects = subjects  # Dictionary: {'Math': 90, 'English': 85, ...}

    def calculate_percentage(self):
        # Total marks divided by number of subjects
        total = sum(self.subjects.values())
        return total / len(self.subjects)

    def display_report(self):
        # Show student info and marks
        self.display_info()
        print("\nSubject Marks:")
        for subject, marks in self.subjects.items():
            print(f"{subject}: {marks} marks")

        # Calculate and display percentage
        percentage = self.calculate_percentage()
        print(f"\nPercentage: {percentage:.2f}%")

        # Assign grade based on percentage
        if percentage >= 80:
            grade = 'A'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 40:
            grade = 'C'
        else:
            grade = 'F'

        print(f"Grade: {grade}")

# Main function to run the app
def main():
    print("Welcome to the Report Card Generator!")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    subjects = {}

    # Input number of subjects and marks
    n = int(input("How many subjects? "))
    for _ in range(n):
        subject = input("Enter subject name: ")
        marks = int(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    # Create object and show report
    student = ReportCard(name, roll_no, subjects)
    student.display_report()

# Entry point
if __name__ == "__main__":
    main()
