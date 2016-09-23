class Solution(object):
    def num_tree(self, n):
        if n == 0:
            return 1
        unique = [0] * (n + 1)
        unique[0] = unique[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                unique[i] += unique[j - 1] * unique[i - j]
        return unique[n]