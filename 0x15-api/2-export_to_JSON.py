#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


def exp_to_json(emp_id):
    """get employee progress"""
    base = f"https://jsonplaceholder.typicode.com"
    url = f"{base}/todos?userId={emp_id}"
    res = requests.get(url)

    if res.status_code == 200:
        tasks = res.json()
        name = requests.get(f"{base}/users/{emp_id}").json().get("username")
        json_filename = f"{emp_id}.json"
        data = {str(emp_id): [{"task": task.get("title"), "completed":
                task.get("completed"), "username": name} for task in tasks]}

        with open(json_filename, mode='w') as f:
            json.dump(data, f)
    else:
        print("Error")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    exp_to_json(employee_id)
