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
        # Parse the command-line argument
        n = int(sys.argv[1])
        if n < 0:
            print("Error: Input must be a non-negative integer.")
        else:
            f = factorial(n)
            print(f)
    except (IndexError, ValueError):
        print("Usage: ./factorial.py <non-negative integer>")
