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
menu()

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

app.py

import streamlit as st

# Create a class for the To-Do List
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
        return self.tasks


# Create an instance of the To-Do List
todo_list = TodoList()

# Streamlit App
st.title("📝 My To-Do List Web App")
st.write("Add, Remove or View Your Tasks Here.")

# Input Field to Add Task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task:
        todo_list.add_task(new_task)
        st.success(f'Task "{new_task}" added!')
    else:
        st.warning("Please enter a task.")

# Show Current Tasks
st.subheader("Your Tasks:")
tasks = todo_list.show_tasks()
if not tasks:
    st.write("✅ No tasks in the to-do list.")
else:
    for task in tasks:
        col1, col2 = st.columns([4, 1])
        col1.write(f"📝 {task}")
        if col2.button(f"❌ Remove {task}"):
            todo_list.remove_task(task)
            st.experimental_rerun()

# Footer
st.markdown("""
---
✅ Built by [Pratik Sutradhar](https://www.linkedin.com/in/pratik-sutradhar)
💻 Powered by Streamlit
""")