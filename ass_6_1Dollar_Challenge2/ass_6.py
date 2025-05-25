# _________ TO DO TASK MANAGER____________

# Class to represent a single task
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False  # Default status is incomplete

    def mark_done(self):
        self.completed = True  # Change status to complete

# Class to manage all tasks
class TaskManager:
    def __init__(self):
        self.tasks = []  # List to store all tasks

    def add_task(self, title):
        task = Task(title)  # Create new task object
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks added yet.")
            return
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task.completed else "Not Done"
            print(f"{i}. {task.title} - {status}")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print(f"Task '{self.tasks[index].title}' marked as done.")
        else:
            print("Invalid task number!")

# Main function
def main():
    print("Welcome to the To-Do Task Manager")
    manager = TaskManager()

    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            try:
                task_num = int(input("Enter task number to mark as done: "))
                manager.mark_task_done(task_num - 1)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Entry point
if __name__ == "__main__":
    main()


