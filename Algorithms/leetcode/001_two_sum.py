__author__ = 'Liang Li'

# Time O(n**2), cannot use index() method since it returns the lowest index for same items
class Solution1:
    def two_sum(self, nums, target):
        for num in nums:
            if target-num in nums:
                return nums.index(num), nums.index(target-num)

s1 = Solution1()
index1, index2 = s1.two_sum([2, 32, 3, 12, 3, 1, 9], 5)
print(index1+1, index2+1)

# Time O(n)
class Solution2:
    def two_sum(self, nums, target):
        dict = {}
        index = 0
        for num in nums:
            if dict.get(target-num, None) is None:
                dict[num] = index
            else:
                return dict[target-num]+1, index+1
            index += 1

s2 = Solution2()
index1, index2 = s2.two_sum([3, 2, 4], 6)
print(index1, index2)
