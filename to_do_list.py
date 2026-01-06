tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\nOptions: 1-Add 2-Delete 3-View 4-Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        show_tasks()
        try:
            task_no = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_no-1)
            print(f"Removed task: {removed}")
        except:
            print("Invalid number!")
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
