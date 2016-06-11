class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                live_neighbors = self.live_neighbors(board, i, j, row, col)
                if board[i][j] == 1 and 2 <= live_neighbors <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2

        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1

    def live_neighbors(self, board, i, j, row, col):
        lives = 0
        for m in range(max(0, i-1), min(row-1, i+1)+1):
            for n in range(max(0, j-1), min(col-1, j+1)+1):
                lives += board[m][n]&1

        lives -= board[i][j]&1
        return lives


s = Solution()
s.gameOfLife([[0,0]])