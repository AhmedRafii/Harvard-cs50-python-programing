def main():
    tasks = []
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(tasks, task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            view_tasks(tasks)
            index = int(input("Enter the number of the task to mark as done: ")) - 1
            if mark_done(tasks, index):
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            view_tasks(tasks)
            index = int(input("Enter the number of the task to delete: ")) - 1
            if delete_task(tasks, index):
                print("Task deleted.")
            else:
                print("Invalid task number.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False

def view_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i + 1}. {task['task']} [{status}]")
    return tasks

if __name__ == "__main__":
    main()
