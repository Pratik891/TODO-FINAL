# -*- coding: utf-8 -*-
"""Copy of To Do List

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/165oWG2C2rPnb32Ngeb9Ehv7fvYwb55LN
"""

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added!')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed!')
        else:
            print(f'Task "{task}" not found!')

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

# Create an instance of the TodoList
todo_list = TodoList()

def add_task():
    task = input("Enter a task to add: ")
    todo_list.add_task(task)

def remove_task():
    task = input("Enter a task to remove: ")
    todo_list.remove_task(task)

def show_tasks():
    todo_list.show_tasks()

def menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()