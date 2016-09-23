class Solution(object):
    def unique_paths(self, m, n):
        paths = [[0]*n for i in range(m)]
        for i in range(1, m):
            paths[i][0] = 1
        for j in range(1, n):
            paths[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i][j-1]+paths[i-1][j]
        return paths[m-1][n-1]
