__author__ = 'liangl2'
class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        path_num = [[0 for n in range(col+1)] for m in range(row+1)]
        path_num[1][0] = 1
        for i in range(1, row+1):
            for j in range(1,col+1):
                if not obstacleGrid[i-1][j-1]:
                    path_num[i][j] = path_num[i-1][j]+path_num[i][j-1]
        return path_num[row][col]

    def unique_paths_with_obstacles(self, obstacle_grid):
        row = len(obstacle_grid)
        col = len(obstacle_grid[0])
        path_num = [[0 for n in range(col)] for m in range(row)]

        for i in range(row):
            for j in range(col):
                if not obstacle_grid[i][j]:
                    if i == 0 and j == 0:
                        path_num[i][j] = 1
                    elif i == 0 and j != 0:
                        path_num[i][j] = path_num[i][j-1]
                    elif j == 0 and i != 0:
                        path_num[i][j] = path_num[i-1][j]
                    else:
                        path_num[i][j] = path_num[i-1][j]+path_num[i][j-1]
        return path_num[i][j]

s = Solution()
print(s.unique_paths_with_obstacles([[0, 0], [0, 0]]))
print(s.unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
