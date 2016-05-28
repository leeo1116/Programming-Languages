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
        path_len_matrix = [[0]*col_len for i in range(row_len)]
        max_path_len = 0
        for i in range(row_len):
            for j in range(col_len):
                last_dir = -1
                max_path_len = max(max_path_len, self.dfs_search(matrix, i, j,row_len, col_len, last_dir, path_len_matrix))

        return max_path_len

    def dfs_search(self, matrix, i, j, row_len, col_len, last_dir, path_len_matrix):
        if path_len_matrix[i][j]:  # Key step: avoid duplicate calculation of each element
            return path_len_matrix[i][j]
        path_len_r, path_len_d, path_len_l, path_len_u = 0, 0, 0, 0
        direction = [not (j == col_len-1), not (i == row_len-1), not (j == 0), not (i == 0)]
        if last_dir != -1:
            direction[last_dir] = 0
        if direction[0] and matrix[i][j] < matrix[i][j+1]:
            path_len_r = self.dfs_search(matrix, i, j+1, row_len, col_len, 2, path_len_matrix)
        if direction[1] and matrix[i][j] < matrix[i+1][j]:
            path_len_d = self.dfs_search(matrix, i+1, j, row_len, col_len, 3, path_len_matrix)
        if direction[2] and matrix[i][j] < matrix[i][j-1]:
            path_len_l = self.dfs_search(matrix, i, j-1, row_len, col_len, 0, path_len_matrix)
        if direction[3] and matrix[i][j] < matrix[i-1][j]:
            path_len_u = self.dfs_search(matrix, i-1, j, row_len, col_len, 1, path_len_matrix)
        path_len_matrix[i][j] = 1 + max(path_len_r, path_len_d, path_len_l, path_len_u)
        return path_len_matrix[i][j]

s = Solution()
matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],
          [40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],
          [80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],
          [120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
#
# matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
#           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
#           [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
#           [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
#           ]
print(s.longestIncreasingPath(matrix))


""" *******************************************Draft solution********************************************************"""
# class Solution(object):
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         if not matrix:
#             return 0
#         row_len = len(matrix)
#         col_len = len(matrix[0])
#
#         max_path_len = 0
#         for i in range(row_len):
#             for j in range(col_len):
#                 flag = 0  # 1 for increasing, 0 for equal, -1 for decreasing
#                 last_dir = 4
#                 max_path_len = max(max_path_len, self.dfs_search(matrix, i, j, last_dir, flag))
#
#         return max_path_len
#
#     def dfs_search(self, matrix, i, j, last_dir, flag):
#         if not matrix:
#             return 0
#         row_len = len(matrix)
#         col_len = len(matrix[0])
#         direction = [1, 1, 1, 1, 1]
#         direction[last_dir] = 0
#         if i == 0:
#             direction[3] = 0
#         if j == 0:
#             direction[2] = 0
#         if i == row_len-1:
#             direction[1] = 0
#         if j == col_len-1:
#             direction[0] = 0
#         if direction == [0, 0, 0, 0]:
#             return 0
#         path_len_r, path_len_d, path_len_l, path_len_u = 0, 0, 0, 0
#         for k, d in enumerate(direction):
#             if k == 0 and d:
#                 last_dir_r = 2
#                 if matrix[i][j] < matrix[i][j+1]:
#                     flag_r = 1
#                 elif matrix[i][j] == matrix[i][j+1]:
#                     flag_r = 0
#                 else:
#                     flag_r = -1
#
#                 if flag == 0 and flag_r != 0:
#                     flag_new_r = flag_r
#                 elif flag_r == 0 or flag != flag_r:
#                     continue
#                 else:
#                     flag_new_r = flag
#
#                 path_len_r = self.dfs_search(matrix, i, j+1, last_dir_r, flag_new_r)
#
#             if k == 1 and d:
#                 last_dir_d = 3
#                 if matrix[i][j] < matrix[i+1][j]:
#                     flag_d = 1
#                 elif matrix[i][j] == matrix[i+1][j]:
#                     flag_d = 0
#                 else:
#                     flag_d = -1
#
#                 if flag == 0 and flag_d != 0:
#                     flag_new_d = flag_d
#                 elif flag_d == 0 or flag != flag_d:
#                     continue
#                 else:
#                     flag_new_d = flag
#
#                 path_len_d = self.dfs_search(matrix, i+1, j, last_dir_d, flag_new_d)
#
#             if k == 2 and d:
#                 last_dir_l = 0
#                 if matrix[i][j] < matrix[i][j-1]:
#                     flag_l = 1
#                 elif matrix[i][j] == matrix[i][j-1]:
#                     flag_l = 0
#                 else:
#                     flag_l = -1
#
#                 if flag == 0 and flag_l != 0:
#                     flag_new_l = flag_l
#                 elif flag_l == 0 or flag != flag_l:
#                     continue
#                 else:
#                     flag_new_l = flag
#
#                 path_len_l = self.dfs_search(matrix, i, j-1, last_dir_l, flag_new_l)
#
#             if k == 3 and d:
#                 last_dir_u = 1
#                 if matrix[i][j] < matrix[i-1][j]:
#                     flag_u = 1
#                 elif matrix[i][j] == matrix[i-1][j]:
#                     flag_u = 0
#                 else:
#                     flag_u = -1
#
#                 if flag == 0 and flag_u != 0:
#                     flag_new_u = flag_u
#                 elif flag_u == 0 or flag != flag_u:
#                     continue
#                 else:
#                     flag_new_u = flag
#
#                 path_len_u = self.dfs_search(matrix, i-1, j, last_dir_u, flag_new_u)
#
#         return 1+max(path_len_r, path_len_d, path_len_l, path_len_u)
