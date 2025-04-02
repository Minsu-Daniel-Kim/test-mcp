#!/usr/bin/env python3
"""
A simple script to calculate Fibonacci numbers.
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to the nth number.
    
    Args:
        n (int): The number of Fibonacci numbers to generate
        
    Returns:
        list: A list of Fibonacci numbers
    """
    return [fibonacci(i) for i in range(n)]

if __name__ == "__main__":
    # Example usage
    n = 10
    print(f"Fibonacci({n}) = {fibonacci(n)}")
    print(f"Fibonacci sequence up to {n}: {fibonacci_sequence(n)}")