# test-mcp

Test repository for MCP functionality with Fibonacci implementations.

## Implementations

This repository contains different implementations of the Fibonacci sequence algorithm:

### Main Branch
- `fibonacci.py`: Iterative implementation

### Alternative Branch
- `fibonacci_recursive.py`: Recursive implementation with memoization

## Usage

Both implementations provide:
- A function to calculate the nth Fibonacci number
- A function to generate a sequence of Fibonacci numbers

### Example

```python
# Using the iterative implementation
from fibonacci import fibonacci, fibonacci_sequence

# Get the 10th Fibonacci number
fib_10 = fibonacci(10)

# Get the sequence up to 10
sequence = fibonacci_sequence(10)
```

## Performance

The recursive implementation with memoization is included in the alternative-fibonacci branch as it provides similar performance to the iterative approach but uses a different technique.