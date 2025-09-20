import argparse
from grid import GridEnvironment
from search import bfs, uniform_cost_search, a_star, hill_climbing

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", choices=["bfs", "ucs", "astar", "hill"], required=True)
    args = parser.parse_args()

    grid = [
        [1,1,1,1,1],
        [1,9,9,9,1],
        [1,1,1,9,1],
        [1,9,1,1,1],
        [1,1,1,1,1],
    ]
    start, goal = (0,0), (4,4)
    env = GridEnvironment(grid, start, goal)

    if args.algo == "bfs":
        path = bfs(env)
        print("BFS Path:", path)
    elif args.algo == "ucs":
        path, cost = uniform_cost_search(env)
        print("UCS Path:", path, "Cost:", cost)
    elif args.algo == "astar":
        path, cost = a_star(env)
        print("A* Path:", path, "Cost:", cost)
    elif args.algo == "hill":
        path, cost = hill_climbing(env)
        print("Hill-Climbing Path:", path, "Cost:", cost)

if _name_ == "_main_":
    main()
