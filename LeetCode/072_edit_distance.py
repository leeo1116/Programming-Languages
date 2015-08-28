__author__ = 'liangl2'
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        edit_distance = [[0 for j in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            edit_distance[i][0] = i
        for j in range(1, n+1):
            edit_distance[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    edit_distance[i][j] = edit_distance[i-1][j-1]
                else:
                    edit_distance[i][j] = min(edit_distance[i-1][j-1], edit_distance[i][j-1], edit_distance[i-1][j])+1
        return edit_distance[-1][-1]