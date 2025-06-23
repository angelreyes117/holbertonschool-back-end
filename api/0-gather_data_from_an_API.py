#!/usr/bin/python3
"""
This script gathers data from the JSONPlaceholder API for a given employee ID
and displays their TODO list progress in a specific format.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    if response.status_code != 200:
        print(f"Error: User with ID {employee_id} not found")
        sys.exit(1)
    user_data = response.json()
    employee_name = user_data.get('name', 'Unknown')

    # Fetch TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for user {employee_id}")
        sys.exit(1)
    todos = response.json()

    # Calculate task progress
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo.get('completed', False))

    # Print progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo.get('completed', False):
            print(f"\t {todo.get('title', '')}")
