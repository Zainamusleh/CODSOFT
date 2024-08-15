tasks = []

def show_menu():
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Task: ")
    tasks.append({"title": title, "completed": False})
    print(f"Added: {title}")

def complete_task():
    view_tasks()
    num = int(input("Task number to complete: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1]['completed'] = True
        print(f"Completed: {tasks[num - 1]['title']}")

def delete_task():
    view_tasks()
    num = int(input("Task number to delete: "))
    if 1 <= num <= len(tasks):
        print(f"Deleted: {tasks.pop(num - 1)['title']}")

while True:
    show_menu()
    choice = input("Choose (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
