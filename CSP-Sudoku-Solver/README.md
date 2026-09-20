# CSP Sudoku Solver

A Python implementation of a Sudoku solver that treats the puzzle as a Constraint Satisfaction Problem (CSP). By defining the board through variables, domains, and constraints, this program uses constraint propagation and search algorithms to efficiently find solutions to even the hardest Sudoku puzzles.

## 🧠 How It Works

A standard Sudoku board is an 81-variable CSP:
* **Variables:** The 81 squares on the board, labeled A1 through I9.
* **Domains:** The digits `1` through `9`.
* **Constraints:** The *AllDiff* constraint applies to each unit. No digit can be repeated in any given row, column, or 3x3 box.

The solver employs two primary AI strategies to find the solution:
1.  **Constraint Propagation:** As a value is assigned to a square, it is immediately eliminated from the domains of all its peers (squares in the same row, column, and box). If a square is reduced to a single possible value, that value is assigned, and the elimination continues.
2.  **Backtracking Search:** For puzzles that cannot be solved by propagation alone, the algorithm selects the square with the fewest remaining possibilities and systematically guesses a value, backtracking if it hits a dead end.

## ✨ Features

* **Zero Dependencies:** Written in pure Python. No external libraries required.
* **Highly Efficient:** Solves most puzzles in fractions of a second using advanced pruning techniques.
* **Text-Based UI:** Clean console output displaying the grid before and after solving.

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your system.

### Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/CSP-Sudoku-Solver.git](https://github.com/yourusername/CSP-Sudoku-Solver.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd CSP-Sudoku-Solver
   ```
3. Run the solver:
   ```bash
   python CSP-Sudoku-Solver.py
   ```
