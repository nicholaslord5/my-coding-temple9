tasks = []

def display_menu():
    print("\nYour To-Do List App is Ready!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    title = input("Enter the task title: ").strip()
    if title:
        tasks.append({"title": title, "status": "Incomplete"})
        print(f'Task "{title}" has been added.')
    else:
        print("Task title cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for t, task in enumerate(tasks, 1):
            print(f"{t}. {task['title']} - {task['status']}")

def mark_task_complete():

    try:
        view_tasks()
        if not tasks:
            return
        
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Complete"
            print(f'Task "{tasks[task_num - 1]["title"]}" is complete.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():

    try:
        view_tasks()
        if not tasks:
            return
        
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task["title"]}" is deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def quit_app():

    print("Thank you for using this to-do list app. Happy Tasking!")
    exit()

def main():

    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                mark_task_complete()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                quit_app()
            else:
                print("Invalid choice. Please select a valid option.")
        except KeyboardInterrupt:
            print("\nApplication interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()