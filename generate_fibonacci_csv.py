#!/usr/bin/env python3
"""
Script to generate a large CSV file with Fibonacci numbers.
"""
import csv
import time

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an efficient iterative approach.
    
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

def generate_fibonacci_csv(filename, count=1000000):
    """
    Generate a CSV file with Fibonacci numbers.
    
    Args:
        filename (str): The name of the CSV file to create
        count (int): The number of Fibonacci numbers to generate
    """
    print(f"Generating {count} Fibonacci numbers to {filename}...")
    start_time = time.time()
    
    # Use chunk size to avoid memory issues with large sequences
    chunk_size = 10000
    num_chunks = count // chunk_size + (1 if count % chunk_size > 0 else 0)
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Index', 'Fibonacci Number'])
        
        # Process in chunks to manage memory
        for chunk in range(num_chunks):
            start_idx = chunk * chunk_size
            end_idx = min(start_idx + chunk_size, count)
            
            # Generate and write one chunk
            for i in range(start_idx, end_idx):
                if i % 100000 == 0 and i > 0:
                    elapsed = time.time() - start_time
                    print(f"Progress: {i}/{count} ({i/count*100:.2f}%) - Time elapsed: {elapsed:.2f}s")
                
                # For very large indices, we'll use a formula approximation to avoid overflow
                if i > 1000:
                    # Using Binet's formula with rounding for large indices
                    import math
                    phi = (1 + math.sqrt(5)) / 2
                    fib_approx = int(round((phi**i - (1-phi)**i) / math.sqrt(5)))
                    writer.writerow([i, fib_approx])
                else:
                    writer.writerow([i, fibonacci(i)])
    
    total_time = time.time() - start_time
    print(f"Done! Generated {count} numbers in {total_time:.2f} seconds")
    print(f"File saved as {filename}")

if __name__ == "__main__":
    # Generate 1M records
    generate_fibonacci_csv("fibonacci_1M.csv", 1000000)