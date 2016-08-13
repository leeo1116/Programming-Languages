class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum)//2
            if half:
                left = sort(enum[:half])
                right = sort(enum[half:])
                for i in range(len(enum)-1, -1, -1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0]*len(nums)
        sort(list(enumerate(nums)))
        return smaller


s = Solution()
print(s.countSmaller([5, 2, 6, 1]))
