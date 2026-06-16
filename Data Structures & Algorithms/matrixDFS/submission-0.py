class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if (len(grid) <= 0):
            return 0
        visited = set()
        island = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if (cell == 1):
                    if ((i, j) in visited):
                        continue
                    visited.add((i, j))
                    island += 1
                    self.dfs(grid, i, j, visited)
        return island
    def dfs(self, grid, i, j, visited):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if (self.outOfBound(grid, x, y)):
                continue
            if (grid[x][y] == 0):
                continue
            if ((x, y) in visited):
                continue
            visited.add((x, y))
            self.dfs(grid, x, y, visited)
    def outOfBound(self, grid, i, j):
        num_row = len(grid)
        num_col = len(grid[0])
        if (i < 0) or (i > num_row - 1):
            return True
        if (j < 0) or (j > num_col - 1):
            return True
        return False
