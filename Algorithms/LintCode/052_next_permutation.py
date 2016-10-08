class Solution(object):
    def next_permutation(self, num):
        num_len, partition_index = len(num), -1
        for i in range(num_len-1, 0, -1):
            if num[i-1] < num[i]:
                partition_index = i-1
                break
        if partition_index != -1:
            for j in range(num_len-1, partition_index, -1):
                if num[j] > num[partition_index]:
                    num[partition_index], num[j] = num[j], num[partition_index]
                    break
        m, n = partition_index+1, num_len-1
        while m < n:
            num[m], num[n] = num[n], num[m]
            m += 1
            n -= 1
        return num


s = Solution()
print(s.next_permutation([]))
