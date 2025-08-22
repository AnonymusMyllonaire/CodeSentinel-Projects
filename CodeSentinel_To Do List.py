import json
import os

TASKS_FILE = "tasks.json"

# ---------- Utility functions ----------
def load_tasks():
    """Load tasks from the JSON file (or return empty list)."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)  # returns a list
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """Save the tasks list into the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# ---------- App features ----------
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("❌ Task cannot be empty.\n")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.\n")
        return
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Removed task: {removed}\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
    else:
        print("\n📋 To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# ---------- Main Loop ----------
def main():
    tasks = load_tasks()
    while True:
        print("=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
