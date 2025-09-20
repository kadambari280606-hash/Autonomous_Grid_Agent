def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(env):
    frontier = [(0, env.start)]
    came_from = {env.start: None}
    cost_so_far = {env.start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == env.goal:
            break
        for nxt in env.neighbors(current):
            new_cost = cost_so_far[current] + env.cost(nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                priority = new_cost + heuristic(nxt, env.goal)
                heapq.heappush(frontier, (priority, nxt))
                came_from[nxt] = current
    return reconstruct_path(came_from, env.start, env.goal), cost_so_far.get(env.goal, float("inf"))
