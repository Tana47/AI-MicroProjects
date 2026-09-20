# Uninformed Search Strategies: 8-Queens Performance Comparison

This repository explores and benchmarks fundamental uninformed (blind) search algorithms by applying them to the classic **8-Queens Problem**. 



The goal of the 8-Queens problem is to place eight chess queens on an 8x8 chessboard so that no two queens threaten each other. This project uses this constraint satisfaction problem as a testing ground to compare the efficiency, time complexity, and space complexity of different state-space search strategies.

## Algorithms Implemented & Compared
* **BFS (Breadth-First Search):** Explores the search tree level by level. Guaranteed to find the shortest path but is highly memory-intensive.
* **DFS (Depth-First Search):** Dives deep into a path before backtracking. Highly memory-efficient but not guaranteed to find the optimal path in generic scenarios.
* **UCS (Uniform-Cost Search):** Expands the least-cost node. In this unweighted problem, it functions similarly to BFS.
* **DLS (Depth-Limited Search):** A variant of DFS with a strict depth boundary (Limit=8) to prevent infinite loops.
* **IDDFS (Iterative Deepening DFS):** Combines the memory efficiency of DFS with the completeness of BFS by incrementally increasing the depth limit.

## Prerequisites
* **Python 3.x**
* No external dependencies or packages are required. The script relies purely on Python's standard library (`time`, `collections.deque`, and `heapq`).

## How to Run
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
