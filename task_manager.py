tasks = []


def add_task(task):
    if not task.strip():
        raise ValueError("Task cannot be empty.")

    tasks.append(task.strip())
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def delete_task(task_number):
    try:
        task_number = int(task_number)

        if task_number < 1 or task_number > len(tasks):
            raise ValueError("Invalid task number.")

        removed_task = tasks.pop(task_number - 1)
        print(f"Deleted: {removed_task}")

    except ValueError:
        print("Please enter a valid task number.")