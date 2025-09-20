# Autonomous_Grid_Agent
The program implements a Grid Environment where a start state and goal state are defined. Obstacles are represented in the grid, and the task is to find a valid route from the start to the goal. The project integrates multiple classical search algorithms, making it useful for studying and comparing their performance.

Autonomous Delivery Agent with Pathfinding Algorithms
Project Overview
This project designs and implements an autonomous delivery agent that navigates a 2D grid city to deliver packages efficiently. The agent must handle various constraints such as static obstacles, varying terrain costs, and dynamic moving obstacles. The system demonstrates different search strategies in Artificial Intelligence, ranging from uninformed search to informed and local search methods.

Features
Environment Modeling
Static obstacles (buildings, blocked roads).
Varying terrain costs (roads, rough terrains, traffic zones).
Dynamic obstacles (moving vehicles or pedestrians).

Agent Properties

Rational decision-making: chooses actions to maximize delivery efficiency under constraints such as time and fuel.
Replanning ability: adapts when new dynamic obstacles appear.

Implemented Algorithms

Uninformed Search: Breadth-First Search (BFS), Uniform Cost Search (UCS).
Informed Search: A* Search with admissible heuristics.
Local Search / Replanning: Hill-Climbing with random restarts or Simulated Annealing (for dynamic environments).

Performance Comparison

Collects and reports metrics such as path cost, nodes expanded, and computation time.
Experimental results across different maps (small, medium, large, dynamic).
