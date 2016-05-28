class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        row_len = len(matrix)
        col_len = len(matrix[0])

        max_path_len = 0
        for i in range(row_len):
            for j in range(col_len):
                flag = 0  # 1 for increasing, 0 for equal, -1 for decreasing
                last_dir = -1
                max_path_len = max(max_path_len, self.dfs_search(matrix, i, j, row_len, col_len, last_dir, flag))

        return max_path_len

    def dfs_search(self, matrix, i, j, row_len, col_len, last_dir, flag):
        direction = [1, 1, 1, 1]
        if last_dir != -1:
            direction[last_dir] = 0
        if i == 0:
            direction[3] = 0
        if j == 0:
            direction[2] = 0
        if i == row_len-1:
            direction[1] = 0
        if j == col_len-1:
            direction[0] = 0
        if direction == [0, 0, 0, 0]:
            return 0
        path_len_r, path_len_d, path_len_l, path_len_u = 0, 0, 0, 0
        for k, d in enumerate(direction):
            if k == 0 and d:
                last_dir_r = 2
                if matrix[i][j] < matrix[i][j+1]:
                    flag_r = 1
                elif matrix[i][j] == matrix[i][j+1]:
                    flag_r = 0
                else:
                    flag_r = -1

                if flag == 0 and flag_r != 0:
                    flag_new_r = flag_r
                elif flag_r == 0 or flag != flag_r:
                    continue
                else:
                    flag_new_r = flag

                path_len_r = self.dfs_search(matrix, i, j+1, row_len, col_len, last_dir_r, flag_new_r)

            if k == 1 and d:
                last_dir_d = 3
                if matrix[i][j] < matrix[i+1][j]:
                    flag_d = 1
                elif matrix[i][j] == matrix[i+1][j]:
                    flag_d = 0
                else:
                    flag_d = -1

                if flag == 0 and flag_d != 0:
                    flag_new_d = flag_d
                elif flag_d == 0 or flag != flag_d:
                    continue
                else:
                    flag_new_d = flag

                path_len_d = self.dfs_search(matrix, i+1, j, row_len, col_len, last_dir_d, flag_new_d)

            if k == 2 and d:
                last_dir_l = 0
                if matrix[i][j] < matrix[i][j-1]:
                    flag_l = 1
                elif matrix[i][j] == matrix[i][j-1]:
                    flag_l = 0
                else:
                    flag_l = -1

                if flag == 0 and flag_l != 0:
                    flag_new_l = flag_l
                elif flag_l == 0 or flag != flag_l:
                    continue
                else:
                    flag_new_l = flag

                path_len_l = self.dfs_search(matrix, i, j-1, row_len, col_len, last_dir_l, flag_new_l)

            if k == 3 and d:
                last_dir_u = 1
                if matrix[i][j] < matrix[i-1][j]:
                    flag_u = 1
                elif matrix[i][j] == matrix[i-1][j]:
                    flag_u = 0
                else:
                    flag_u = -1

                if flag == 0 and flag_u != 0:
                    flag_new_u = flag_u
                elif flag_u == 0 or flag != flag_u:
                    continue
                else:
                    flag_new_u = flag

                path_len_u = self.dfs_search(matrix, i-1, j, row_len, col_len, last_dir_u, flag_new_u)

        return 1+max(path_len_r, path_len_d, path_len_l, path_len_u)


s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))