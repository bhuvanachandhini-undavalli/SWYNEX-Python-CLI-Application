import task_manager


def show_menu():
    print("\n===== SWYNEX TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
    task = input("Enter task: ")

    try:
        task_manager.add_task(task)
    except ValueError as error:
        print(f"Error: {error}")

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_manager.view_tasks()

            if task_manager.tasks:
                task_number = input("Enter task number to delete: ")
                task_manager.delete_task(task_number)

        elif choice == "4":
            print("Thank you for using SWYNEX Task Manager!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()