#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif (temperature >= 40 and temperature <= 65):
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return f"It's {response} out there!"

def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# def calculator(operation, num1, num2):
#     operation = {
#         "+": num1 + num2
#         "-": num1 - num2
#         "*": num1 * num2
#         "/": num1 / num2
#     }

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Division by zero!")

def calculator(operation, num1, num2):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    operation_function = operations.get(operation)

    if operation_function:
        return operation_function(num1, num2)
    else:
        print("Invalid operation!")
        return None