#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
import sys


def exp_to_csv(emp_id):
    """Export to CSV"""
    base = f"https://jsonplaceholder.typicode.com"
    url = f"{base}/todos?userId={emp_id}"
    res = requests.get(url)

    if res.status_code == 200:
        tasks = res.json()
        name = requests.get(f"{base}/users/{emp_id}").json().get("username")
        csv_filename = f"{emp_id}.csv"

        with open(csv_filename, mode='w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([emp_id, name,
                                 task.get("completed"), task.get("title")])
    else:
        print("Error")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    exp_to_csv(employee_id)
