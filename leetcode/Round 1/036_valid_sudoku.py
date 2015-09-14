__author__ = 'Liang Li'
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board:
            return False
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

s = Solution()
is_valid = s.isValidSudoku([[1, 2, 3, 4, 5, 6, 8, 9, 7], [1, 2, 3, 4, 5, 6, 8, 9, 7], [1, 2, 3, 4, 5, 6, 8, 9, 7],
                 [1, 2, 3, 4, 5, 6, 8, 9, 7], [1, 2, 3, 4, 5, 6, 8, 9, 7], [1, 2, 3, 4, 5, 6, 8, 9, 7],
                 [1, 2, 3, 4, 5, 6, 8, 9, 7], [1, 2, 3, 4, 5, 6, 8, 9, 7], [1, 2, 3, 4, 5, 6, 8, 9, 7]])
print(is_valid)