class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque([(0, 0, 0)])
        visited = set([(0, 0)])
        while queue:
            i, j, path_len = queue.popleft()
            if i == rows - 1 and j == cols - 1:
                return path_len
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y, path_len + 1))
        return -1