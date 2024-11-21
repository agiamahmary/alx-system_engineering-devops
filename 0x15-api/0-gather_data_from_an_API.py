#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":

    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    data = requests.get(user_url)
    emp_nm = data.json().get("name")

    tsks = requests.get(f"{user_url}/todos").json()

    tsk_done = sum([tsk.get('completed') for tsk in tsks])
    no_tsk = len(tsks)

    print(f"Employee {emp_nm} is done with tasks({tsk_done}/{no_tsk}):")

    for tsk in tsks:
        if tsk.get('completed'):
            print(f"\t {tsk.get('title')}")
