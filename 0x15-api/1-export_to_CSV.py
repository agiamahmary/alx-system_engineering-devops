#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
import requests
import sys


if __name__ == "__main__":

    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    data = requests.get(user_url)
    emp_nm = data.json().get("username")

    tsks = requests.get(f"{user_url}/todos").json()

    for tsk in tsks:
        tsk['userName'] = emp_nm

    with open(f'{sys.argv[1]}.csv', 'w', newline='') as csvfile:
        fieldnames = ['userId', 'userName', 'completed', 'title']

        writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames,
                extrasaction='ignore',
                quoting=csv.QUOTE_ALL
            )

        writer.writerows(tsks)
