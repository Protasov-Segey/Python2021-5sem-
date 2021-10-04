#!/usr/bin/env python
# coding: utf-8

def decorator(author):
    def wrapper(func):
        func.author = author
        return func
    return wrapper

@decorator("Serg") # действие равно add2 = decorator("Serg")
def add2(num: int) -> int:
    return num + 2

print(add2.author)

