#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":

    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    data = requests.get(user_url)
    emp_nm = data.json().get("username")

    tsks = requests.get(f"{user_url}/todos").json()

    dict_file = {sys.argv[1]: []}

    for tsk in tsks:
        dict_file[sys.argv[1]].append(
                {
                    "task": tsk.get('title'),
                    "completed": tsk.get('completed'),
                    "username": emp_nm
                }
            )

    with open(f'{sys.argv[1]}.json', 'w', newline='') as jsonfile:
        json.dump(dict_file, jsonfile)
