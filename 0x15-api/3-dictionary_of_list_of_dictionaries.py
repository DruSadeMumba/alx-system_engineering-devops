#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests


def exp_to_json_dict():
    """get employee progress"""
    base_url = f"https://jsonplaceholder.typicode.com/users"
    user_res = requests.get(base_url)

    if user_res.status_code == 200:
        users = user_res.json()
        complete = {}
        for user in users:
            emp_id = str(user.get("id"))
            name = user.get("username")
            url = f"{base_url}/{emp_id}/todos"
            task_res = requests.get(url)

            if task_res.status_code == 200:
                tasks = task_res.json()
                data = [{"username": name, "task": task.get("title"),
                         "completed": task.get("completed")} for task in tasks]
                complete[emp_id] = data
            else:
                print("Task Error")

        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as f:
            json.dump(complete, f)

    else:
        print("User Error")


if __name__ == "__main__":
    exp_to_json_dict()
