__author__ = 'liangl2'
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_recursive(board, word, i, j):
                    return True
        return False

    def exist_recursive(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = ' '
            if i > 0 and self.exist_recursive(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.exist_recursive(board, word[1:], i+1, j):
                return True
            if j > 0 and self.exist_recursive(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.exist_recursive(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0]
            return False
        else:
            return False


