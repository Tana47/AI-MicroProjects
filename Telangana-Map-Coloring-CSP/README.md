# Telangana Map Coloring Problem 🗺️🎨

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Python implementation solving the **Map Coloring Problem** for the 33 districts of Telangana, India. This project models the geographical map as a **Constraint Satisfaction Problem (CSP)** and solves it using a recursive **Backtracking Algorithm**.

## 📖 About the Project

The Map Coloring Problem is a classic computer science and mathematics problem. The objective is to assign a color to each region of a map such that no two adjacent regions (districts sharing a border) have the same color. 

Based on the **Four Color Theorem**, any contiguous planar map can be colored using at most four colors. This script successfully applies this theorem to the state of Telangana, coloring all 33 districts using only a predefined set of four colors: **Red, Green, Blue, and Yellow**.

### Key Features
* **Zero Dependencies:** Written in pure Python. No external libraries (like `networkx` or `pandas`) are required.
* **Geographical Accuracy:** Accurately maps the borders and adjacencies of all 33 reorganized districts of Telangana.
* **Automated Graph Symmetrization:** Automatically ensures bi-directional borders. If District A borders District B, the algorithm inherently enforces that District B borders District A.
* **Efficient Backtracking:** Navigates the constraint tree efficiently, abandoning dead-end color assignments immediately to optimize performance.

## 🚀 Getting Started

### Prerequisites
You only need Python installed on your machine to run this script.
* Python 3.x

### Installation & Usage
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/Telangana-Map-Coloring-CSP.git](https://github.com/yourusername/Telangana-Map-Coloring-CSP.git)
     ```
2. Navigate to the project directory:
   ```bash
   cd Telangana-Map-Coloring-CSP
    ```
3. Run the Python script:
    ```bash
    python Telangana-Map-Coloring-CSP.py
    ```
