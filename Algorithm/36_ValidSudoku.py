# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        a = [[] for x in range(9)]
        b = [[] for x in range(9)]
        c = [[] for x in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                x = board[i][j]
                if x == '.':
                    continue
                if x in a[i] or x in b[j] or x in c[(i // 3) * 3 + (j // 3)]:
                    return False
                a[i].append(x)
                b[j].append(x)
                c[(i // 3) * 3 + (j // 3)].append(x)
        return True
