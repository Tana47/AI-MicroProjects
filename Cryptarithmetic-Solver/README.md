# Cryptarithmetic Solver: TWO + TWO = FOUR

A lightweight Python script that solves the classic cryptarithmetic puzzle **TWO + TWO = FOUR**. 

In this constraint satisfaction problem, each letter represents a distinct digit from 0 to 9. The goal is to find the correct numerical substitution for the letters so that the arithmetic equation holds true, with the rule that leading digits cannot be zero (i.e., 'T' and 'F' cannot be 0).

## Features
* Solves the puzzle using a brute-force permutation approach.
* Utilizes Python's built-in `itertools` library for efficient combinatorial generation.
* Automatically handles the leading-zero constraint.

## Prerequisites
* Python 3.x installed on your machine.
* No external libraries or dependencies are required.

## Usage

1. Clone this repository or download the Python file to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python Cryptarithmetic-Solver.py
   ```
