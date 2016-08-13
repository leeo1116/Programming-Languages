class Solution(object):
    def is_valid_sodoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False

        row, col = len(board), len(board[0])
        # use 3 hash-map to track the uniqueness
        row_element_exist = [[False]*col for i in range(row)]
        col_element_exist = [[False]*col for i in range(row)]
        block_element_exist = [[False]*col for i in range(row)]

        for i in range(row):
            for j in range(col):
                num = board[i][j]
                if num != '.':
                    index = int(num)-1
                    k = i//3*3+j//3
                    if row_element_exist[i][index] or col_element_exist[j][index] or block_element_exist[k][index]:
                        return False
                    row_element_exist[i][index] = col_element_exist[j][index] = block_element_exist[k][index] = True
        return True
