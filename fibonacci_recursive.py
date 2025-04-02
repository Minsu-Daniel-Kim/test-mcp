#!/usr/bin/env python3
"""
A Fibonacci implementation using recursion with memoization.
"""

def fibonacci_recursive(n, memo=None):
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        memo (dict, optional): Memoization dictionary to cache results
        
    Returns:
        int: The nth Fibonacci number
    """
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
        
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
    return memo[n]

def fibonacci_sequence_recursive(n):
    """
    Generate the Fibonacci sequence up to the nth number using the recursive method.
    
    Args:
        n (int): The number of Fibonacci numbers to generate
        
    Returns:
        list: A list of Fibonacci numbers
    """
    # Use a shared memo dictionary for all calculations to improve performance
    memo = {}
    return [fibonacci_recursive(i, memo) for i in range(n)]

if __name__ == "__main__":
    # Compare performance with the original implementation
    import time
    
    n = 30
    
    # Measure recursive with memoization
    start = time.time()
    result = fibonacci_recursive(n)
    end = time.time()
    print(f"Recursive Fibonacci({n}) = {result}")
    print(f"Time taken: {end - start:.6f} seconds")
    
    # Generate and print sequence
    print(f"Fibonacci sequence up to 10: {fibonacci_sequence_recursive(10)}")