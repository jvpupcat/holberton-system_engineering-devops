#!/usr/bin/python3
"""Python script that returns info about employee TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    #setting variables with user and todo data and url
    user_data = {'id': sys.argv[1]}
    user_url = 'https://jsonplaceholder.typicode.com/users'

    todo_data = {'userId': sys.argv[1]}
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    #user data request
    user_request = requests.get(user_url, params=user_data)
    user_json = user_request.json()
    for employee in user_json:
        username = employee['username']

    #get employee todo list
    todo_request = requests.get(todo_url, params=todo_data)
    todo_json = todo_request.json()
    done = 0
    tasks = 0
    tasks_done = []
    for todo in todo_json:
        tasks = tasks + 1
        if todo.get('userId') == user_id:
            done = done + 1
            tasks_done.append(todo.get('title'), todo.get('completed'))
    csv_file = user_id + ".csv"

    #get tasks done and title of it
    for key in todo_json:
        status = key.get('completed')
        title = key.get('title')
        with open(csv_file, 'a+') as f: #open file to read and append
            f.write('"{}","{}","{}","{}"\n'.format
                    (user_id, username, status, title)) #output format
