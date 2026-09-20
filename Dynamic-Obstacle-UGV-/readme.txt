UGV Dynamic Pathfinding Simulation
==================================

OVERVIEW
----------------------------------
This repository contains a Python implementation of a pathfinding algorithm designed for an Unmanned Ground Vehicle (UGV) operating in a simulated 70x70 battlefield grid. The primary objective is to navigate from a start node to a goal node using the shortest possible path while actively avoiding obstacles.

This project specifically addresses the challenge of dynamic obstacles. Unlike static environments where the map is fully known a priori, this simulation introduces obstacles dynamically as the UGV moves, requiring the agent to recalculate its optimal path on the fly.


PROBLEM STATEMENT
----------------------------------
The UGV must navigate a 70x70 grid from a user-specified start node to a goal node. While static obstacles can exist, the core challenge requires the UGV to adapt to a real-world environment where obstacles are dynamic and not known in advance. The algorithm must find the shortest path, avoid obstacles, and trace the route.


APPROACH & ALGORITHM
----------------------------------
The solution utilizes the A* (A-Star) Search Algorithm, a staple in artificial intelligence for finding the shortest path efficiently.

- Heuristic: The algorithm uses the Manhattan Distance heuristic, which is highly effective for grid-based movement where diagonal traversal is not permitted (movement is restricted to Up, Down, Left, Right).

- Dynamic Adaptation: The UGV recalculates its path continuously. After every step, there is a probability (currently set to 10%) that a new obstacle will spawn randomly on the grid. If a new obstacle blocks the previously calculated path, the A* algorithm is invoked again from the UGV's current position to find a new, unblocked route to the goal.


FEATURES
----------------------------------
- 70x70 Grid Environment: Simulates the operational battlefield area.
- A* Pathfinding: Guarantees the shortest path in the current known state of the grid.
- Real-time Obstacle Generation: Introduces dynamic challenges during traversal.
- Live Path Tracing: Outputs the step-by-step movement of the UGV in the console.


MEASURES OF EFFECTIVENESS (MoE)
----------------------------------
When evaluating the performance of this search agent, the following MoEs are considered:
1. Path Length: The total number of steps taken to reach the goal.
2. Completeness: The ability of the algorithm to find the goal if a valid path exists.
3. Adaptability: The successful recalculation of routes when an unexpected obstacle blocks the immediate path.


HOW TO RUN
----------------------------------
Ensure you have Python 3.x installed on your system. No external libraries are required, as the code relies purely on Python's standard heapq, random, and math libraries.

1. Clone the repository or download the program.py file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script using the command: python program.py