#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

if __name__ == "__main__":
    try:
        # Ensure the script is executed with a valid integer argument
        f = factorial(int(sys.argv[1]))
        print(f)
    except (IndexError, ValueError):
        print("Usage: ./factorial.py <non-negative integer>")
