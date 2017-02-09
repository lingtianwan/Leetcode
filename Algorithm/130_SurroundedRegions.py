# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x < 0 or x > m-1 or y < 0 or y > n-1 or board[x][y] != 'O':
                return
            queue.append((x, y))
            board[x][y] = 'D'
        def bfs(x, y):
            if board[x][y] == 'O':
                queue.append((x, y))
                fill(x, y)
            while queue:
                cur = queue.pop(0)
                i = cur[0]
                j = cur[1]
                fill(i, j+1)
                fill(i, j-1)
                fill(i+1, j)
                fill(i-1, j)
        if len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        queue = []
        for i in range(n):
            bfs(0, i)
            bfs(m-1, i)
        for i in range(1, m-1):
            bfs(i, 0)
            bfs(i, n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return
