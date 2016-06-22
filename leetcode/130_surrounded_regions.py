class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0:
            return
        col = len(board[0])

        for i in range(row):
            self.check(board, i, 0, row, col)
            if col > 1:
                self.check(board, i, col-1, row, col)

        for j in range(col):
            self.check(board, 0, j, row, col)
            if row > 1:
                self.check(board, row-1, j, row, col)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'S':
                    board[i][j] = 'O'


    def check(self, board, i, j, row, col):
        if board[i][j] == 'O':
            board[i][j] = 'S'
            if i > 1:
                self.check(board, i-1, j, row, col)
            if j > 1:
                self.check(board, i, j-1, row, col)
            if i < row-1:
                self.check(board, i+1, j, row, col)
            if j < col-1:
                self.check(board, i, j+1, row, col)

