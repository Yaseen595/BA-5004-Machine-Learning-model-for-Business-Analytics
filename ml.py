# -*- coding: utf-8 -*-
"""Ml.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VG3jK4shZAiPsPbUFzRKDe53UYM6LXIA

**Muhammad Ghulam Ali (24I-7335)**
"""

# Function to calculate the square of a number
def calculate_square(number):
    return number * number


calculate_square(5)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

add(5,5),subtract(5,5),multiply(5,5),divide(5,5)

# TODO: Add a feature to greet each team member individually

# Pseudocode:
# 1. Ask user for username and password
# 2. Verify credentials
# 3. Grant access if correct, else show error

# Function to find the maximum among three numbers
def find_maximum(a, b, c):
    return max(a, b, c)

find_maximum(2,9,3)

# Dictionary

student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

print(student)
print("Student Name:", student["name"])