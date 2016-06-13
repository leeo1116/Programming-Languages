class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        count = 0
        for k in range(row):
            grid[k] = list(grid[k])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.mark_land_DFS(grid, i, j, row, col)
                    count += 1
        return count

    def mark_land_DFS(self, grid, m, n, r, c):
        if m < 0 or n < 0 or m >= r or n >= c or grid[m][n] != '1':
            return
        grid[m][n] = '0'
        self.mark_land_DFS(grid, m+1, n, r, c)
        self.mark_land_DFS(grid, m-1, n, r, c)
        self.mark_land_DFS(grid, m, n+1, r, c)
        self.mark_land_DFS(grid, m, n-1, r, c)


s = Solution()
grid = ["11110", "11010", "11000", "00000"]
print(s.numIslands(grid))
