#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    response = requests.get(f"{base_url}/users/{employee_id}")
    if response.status_code != 200:
        print(f"Failed to retrieve employee information. Error: {response.status_code}")
        return

    employee_data = response.json()
    employee_name = employee_data['name']

    # Get employee's TODO list
    response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list. Error: {response.status_code}")
        return

    todos = response.json()
    total_tasks = len(todos)

    # Filter completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]

    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = int(sys.argv[1])

    get_employee_todo_progress(employee_id)


if __name__ == "__main__":
    main()



