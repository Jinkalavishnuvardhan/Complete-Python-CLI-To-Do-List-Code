def show_menu():
    print("""
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
""")

tasks = []

def add_task():
    task_desc = input("Enter task description: ")
    tasks.append({'task': task_desc, 'done': False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t['done'] else "✗"
        print(f"{i}. [{status}] {t['task']}")

def mark_complete():
    view_tasks()
    try:
        choice = int(input("Enter task number to complete: "))
        tasks[choice-1]['done'] = True
        print("Task marked as complete.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        removed = tasks.pop(choice-1)
        print(f"Removed task: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid selection.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
