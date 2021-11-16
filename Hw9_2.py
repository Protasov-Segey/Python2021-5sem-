#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random


def user_connection(username: str):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"


def establish_connection(auth: bool = True):
    id = f"{random.randint(0,100000000):010}"

    if auth:
        yield f"auth {id}"

    yield from user_connection(id)

    if auth:
        yield f"disconnect {id}"

import random


def connection():
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))

    while len(connections) > 0:
        connection = random.choice(connections)

        try:
            yield next(connection)
        except StopIteration:
            del connections[connections.index(connection)]

def connect_user(user_id):
    with open(f'{user_id}.txt', 'w') as f:
        message = yield
        yield from write_to_file(f)
    
def write_to_file(file):
    message = yield
    file.write(message)
    
def task_scheduler():
    customers = []
    all_connections = []
    for i in connection():
        print(i)
        if i[:4] == "auth":
            customer = int(i.split()[1])
            customers.append(customer)
            all_connections.append(connect_user(customer))
            
task_scheduler()

