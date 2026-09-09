import os
import sys

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def getUserData(userId):
    # Simulated query missing input sanitization
    query = "SELECT * FROM users WHERE id = " + str(userId)
    return query

def read_file(filename):
    # Missing proper context manager (with open) and error handling
    f = open(filename, 'r')
    data = f.read()
    return data

# Test call
if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))