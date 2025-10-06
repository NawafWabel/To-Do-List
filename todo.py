## Python Program for Practicals
print("This Program is for Collecting Notes")

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option only between (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("✅ Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\n📋 Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\n📋 Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter the task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Task deleted: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")


