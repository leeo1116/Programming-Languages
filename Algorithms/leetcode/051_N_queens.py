__author__ = 'Liang Li'
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queen_stack, solution = [[(0, i) for i in range(n)]], []
        while queen_stack:
            board = queen_stack.pop()
            row = len(board)
            if row == n:
                solution.append([''.join('Q' if i == c else '.' for i in range(n)) for r, c in board])
            for col in range(n):
                if all(col != c and abs(row-r) != abs(col-c) for r, c in board):
                    queen_stack.append(board+[(row, col)])
        return len(solution)


s = Solution()
print(s.solveNQueens(3))