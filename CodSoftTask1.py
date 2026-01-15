# TO DO LIST

'''A To-Do List application is a useful
project that helps users manage and
organize their tasks efficiently. This project aims to
create a command-line or GUI-based application using Python,
allowing users to create, update, and track their to-do lists'''

import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low/Medium/High): ")
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} [{status}] - Due: {task['due_date']} Priority: {task['priority']}")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter task number to mark as completed: "))
    if 0 < task_no <= len(tasks):
        tasks[task_no - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
