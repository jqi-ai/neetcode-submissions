class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        present = False
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(covid, character, visited, word_index):
            nonlocal present
            nonlocal dirs
            if present == True:
                return
            if covid in visited:
                return
            if character != word[word_index]:
                return
            visited.add(covid)
            word_index += 1
            if word_index == len(word):
                present = True
                return
            x, y = covid
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    dfs((nx, ny), board[nx][ny], visited, word_index)
            visited.remove(covid)
            
        for i, row in enumerate(board):
            for j, character in enumerate(row):
                dfs((i, j), character, set(), 0)
        return present