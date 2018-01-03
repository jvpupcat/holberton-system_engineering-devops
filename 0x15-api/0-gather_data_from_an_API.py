#!/usr/bin/python3
"""Python script that returns info about employee TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    user_data = {'id': sys.argv[1]}
    todo_data = {'userId': sys.argv[1]}
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user_request = requests.get(user_url, params=user_data)
    user_json = user_request.json()
    for employee in user_json:
        name = employee['name']

    todo_request = requests.get(todo_url, params=todo_data)
    todo_json = todo_request.json()
    done = 0
    tasks = 0
    tasks_done = []
    for status in todo_json:
        tasks = tasks + 1
        if status.get('completed') == True:
            done = done + 1
            tasks_done.append(status.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))
    for completed in tasks_done:
        print('\t' + completed)
