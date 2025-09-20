import heapq
import random

class GridEnvironment:
    def _init_(self, grid, start, goal, moving_obstacles=None):
        """
        grid: 2D list of terrain costs (int >= 1)
        start: (row, col)
        goal: (row, col)
        moving_obstacles: list of obstacle paths [(time, (x, y)), ...]
        """
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.moving_obstacles = moving_obstacles or {}

    def in_bounds(self, pos):
        (r, c) = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def cost(self, pos):
        r, c = pos
        return self.grid[r][c]

    def neighbors(self, pos, t=0):
        (r, c) = pos
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        result = []
        for dr, dc in moves:
            nxt = (r+dr, c+dc)
            if self.in_bounds(nxt):
                # avoid moving obstacles
                if (t, nxt) not in self.moving_obstacles:
                    result.append(nxt)
        return result
