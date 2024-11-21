#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests


if __name__ == "__main__":

    users_url = f"https://jsonplaceholder.typicode.com/users/"
    users_data = requests.get(users_url).json()
    all_data = {}

    for user in users_data:
        emp_nm = user.get("username")

        tsks = requests.get(
                f"{users_url}{user.get('id')}/todos").json()

        all_data[user.get('id')] = []
        for tsk in tsks:
            all_data[user.get('id')].append(
                    {
                        "task": tsk.get('title'),
                        "completed": tsk.get('completed'),
                        "username": emp_nm
                    }
                )

    with open(f'todo_all_employees.json', 'w', newline='') as jsonfile:
        json.dump(all_data, jsonfile)
