__author__ = 'liangl2'
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        for c in word:
            for row in board:
                if c in row:
