# test-mcp

Test repository for MCP functionality with Fibonacci implementations.

## Implementations

This repository contains different implementations of the Fibonacci sequence algorithm:

### Main Branch
- `fibonacci.py`: Iterative implementation
- `generate_fibonacci_csv.py`: Script to generate a CSV file with 1 million Fibonacci numbers
- `fibonacci_sample.csv`: Sample CSV with the first 100 Fibonacci numbers

### Alternative Branch
- `fibonacci_recursive.py`: Recursive implementation with memoization

## CSV Generation

The repository includes a script to generate a large CSV file with Fibonacci numbers:

```bash
# Generate 1 million Fibonacci numbers and save to CSV
python generate_fibonacci_csv.py
```

This will create a file called `fibonacci_1M.csv` with 1 million records. The file is quite large, so only a sample is included in the repository.

### CSV Format

The CSV file has the following format:

```
Index,Fibonacci Number
0,0
1,1
2,1
...
```

### Git LFS

The repository is configured with Git LFS to handle large CSV files. When cloning, make sure you have Git LFS installed:

```bash
git lfs install
git clone https://github.com/Minsu-Daniel-Kim/test-mcp.git
```

## Performance Notes

For very large indices (over 1000), the script uses Binet's formula approximation to avoid numeric overflow issues that would occur with direct calculation.