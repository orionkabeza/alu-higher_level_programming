#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
from datetime import datetime
print('This the current date and time: ')
print(datetime.now())

def greet(name: str) -> None:
    print(f"Hello, {name}!")
    greet("Alice")
    greet("Bob")
