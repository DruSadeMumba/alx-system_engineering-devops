#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


def get_progress(emp_id):
    """get employee progress"""
    base = f"https://jsonplaceholder.typicode.com"
    url = f"{base}/todos?userId={emp_id}"
    res = requests.get(url)

    if res.status_code == 200:
        tasks = res.json()
        comp = [task for task in tasks if task["completed"]]
        name = requests.get(f"{base}/users/{sys.argv[1]}").json().get("name")

        print(f"Employee {name} is done with tasks({len(comp)}/{len(tasks)}):")
        for task in comp:
            print(f"\t {task['title']}")
    else:
        print("Error")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    get_progress(employee_id)
