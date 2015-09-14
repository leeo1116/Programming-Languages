__author__ = 'Liang Li'
class Solution1(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in map(str, list(range(1, 10))):

                        if self.is_valid(i, j, c, board):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def is_valid(self, i, j, c, board):
        for row in range(len(board)):
            if board[row][j] == c:
                return False
        for col in range(len(board[0])):
            if board[i][col] == c:
                return False
        for row in range(i//3*3, i//3*3+3):
            for col in range(j//3*3, j//3*3+3):
                if board[row][col] == c:
                    return False
        return True

class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in map(str, list(range(1, 10))):
                        board[i][j] = c
                        if self.is_valid(board):
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    board[i][j] = '.'
                    return False
        return True

    def is_valid(self, board):

        row_hash = [[False]*9 for i in range(9)]
        col_hash = [[False]*9 for i in range(9)]
        block_hash = [[False]*9 for i in range(9)]
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                num = board[i][j]
                if num != '.':
                    index = int(num)-1
                    k = i//3*3+j//3
                    if row_hash[i][index] or col_hash[j][index] or block_hash[k][index]:
                        return False
                    row_hash[i][index] = col_hash[j][index] = block_hash[k][index] = True
        return True

        if not board or len(board) == 0:
            return
        self.solve(board)

# board = [['.']*9 for i in range(9)]
b = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = [['.']*9 for i in range(9)]
for i in range(len(b)):
    board[i] = list(b[i])

s = Solution1()
s.solveSudoku(board)
for i in range(len(board)):
    print(board[i])

