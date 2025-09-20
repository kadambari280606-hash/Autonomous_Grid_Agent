from collections import deque
import heapq

def bfs(env):
    frontier = deque([env.start])
    came_from = {env.start: None}
    while frontier:
        current = frontier.popleft()
        if current == env.goal:
            break
        for nxt in env.neighbors(current):
            if nxt not in came_from:
                frontier.append(nxt)
                came_from[nxt] = current
    return reconstruct_path(came_from, env.start, env.goal)

def uniform_cost_search(env):
    frontier = [(0, env.start)]
    came_from = {env.start: None}
    cost_so_far = {env.start: 0}

    while frontier:
        current_cost, current = heapq.heappop(frontier)
        if current == env.goal:
            break
        for nxt in env.neighbors(current):
            new_cost = cost_so_far[current] + env.cost(nxt)
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, nxt))
                came_from[nxt] = current
    return reconstruct_path(came_from, env.start, env.goal), cost_so_far.get(env.goal, float("inf"))

def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return []
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
