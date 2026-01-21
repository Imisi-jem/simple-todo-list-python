# Simple To-Do List Application

tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

def update_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[task_number - 1] = new_task
            print("Task updated successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("==== Simple To-Do List ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if _name_ == "_main_":
    main()