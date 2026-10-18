# Online and Offline Algorithms Using Python

## Description

This project implements two algorithms in Python and connects them through a third Python file (`main.py`).

The project demonstrates online load balancing across multiple processors and matrix-chain multiplication using dynamic programming. A menu-driven main program allows users to select and execute either algorithm.

## Folder Structure

```text
Online_Offline_Algorithms/
│
├── online_load_balancing.py
├── matrix_chain_multiplication.py
├── main.py
└── README.md
```

## Technologies Used

- Python 3
- Greedy Algorithm
- Dynamic Programming
- Functions and Modules
- Menu-Driven Programming

## Program 1: Online Load Balancing Across Multiple Processors

**File name:** `online_load_balancing.py`

### Aim

To assign incoming jobs to the processor with the smallest current workload.

### Working

1. Enter the number of processors and jobs.
2. Enter each job's processing time as it arrives.
3. Assign each job to the least-loaded processor.
4. Update the processor's workload.
5. Display the final workloads and maximum workload.

### Time Complexity

`O(m × n)`, where `m` is the number of jobs and `n` is the number of processors.

## Program 2: Matrix-Chain Multiplication Using Dynamic Programming

**File name:** `matrix_chain_multiplication.py`

### Aim

To calculate the minimum number of scalar multiplications required to multiply a chain of matrices.

### Working

1. Enter the number of matrices.
2. Enter the matrix dimensions.
3. Use dynamic programming to calculate multiplication costs.
4. Find the optimal multiplication order.
5. Display the minimum multiplication cost.

### Time Complexity

`O(n³)`

### Space Complexity

`O(n²)`

## Program 3: Main Menu and Program Connection

**File name:** `main.py`

### Aim

To connect Program 1 and Program 2 using Python modules and a menu-driven interface.

### Menu Options

```text
===== ONLINE AND OFFLINE ALGORITHMS =====
1. Online Load Balancing
2. Matrix-Chain Multiplication
3. Exit
```

### Working

- Option 1 calls `online_load_balancing()` from `online_load_balancing.py`.
- Option 2 calls `matrix_chain_multiplication()` from `matrix_chain_multiplication.py`.
- Option 3 exits the application.
- After either algorithm finishes, the menu appears again.

**Important:** Both algorithm files must define the functions imported by `main.py`. Protect their standalone execution with `if __name__ == "__main__":` so that importing them does not run them automatically.

## Learning Outcomes

- Understand online algorithms and greedy job assignment.
- Learn matrix-chain multiplication using dynamic programming.
- Understand Python functions and module imports.
- Connect multiple Python files in one application.
- Develop menu-driven programs.
- Analyze time and space complexity.

## Applications

- Processor scheduling and load balancing.
- Distributed computing.
- Matrix computation.
- Algorithm optimization.
- Design and Analysis of Algorithms (DAA) practical examinations.

## Requirements

- Python 3
- Visual Studio Code or another Python-compatible editor

No external Python packages are required.

## Author

BCA Student

## License

This project is intended for educational and academic practical work.
