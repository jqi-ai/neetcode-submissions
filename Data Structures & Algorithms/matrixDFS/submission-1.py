class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.paths = 0
        if len(grid) <= 0 or grid[0][0] == 1:
            return 0
        self.dfs(grid, 0, 0, {(0, 0)})
        return self.paths

    def dfs(self, grid, i, j, visited):
        if (i == len(grid) - 1) and (j == len(grid[0]) - 1):
            self.paths += 1
            return
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if self.outOfBound(grid, x, y):
                continue
            if (x, y) in visited:
                continue
            if grid[x][y] == 1:
                continue
            visited.add((x, y))
            self.dfs(grid, x, y, visited)
            visited.remove((x, y))
        return

    def outOfBound(self, grid, i, j):
        num_row = len(grid)
        num_col = len(grid[0])
        if i < 0 or i > num_row - 1:
            return True
        if j < 0 or j > num_col - 1:
            return True
        return False