#!/usr/bin/python3
"""
This script gathers data from a REST API for a given employee ID
and returns information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_url = f"{base_url}/users/{employee_id}"
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    # Fetch todos
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos = requests.get(todos_url).json()

    # Count completed and total tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task_title in completed_tasks:
        print("\t {}".format(task_title))
