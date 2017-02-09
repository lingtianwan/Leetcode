# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
#
# Follow up:
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        dx = [0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, 0, -1, 1, 0, -1, 1]
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    lives += self.getCellStatus(board, nx, ny)
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
        return

    def getCellStatus(self, board, nx, ny):
        m = len(board)
        n = len(board[0])
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            return 0
        return board[nx][ny] & 1
