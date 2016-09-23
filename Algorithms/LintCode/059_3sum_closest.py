class Solution(object):
    def three_sum_closest(self, numbers, target):
        """
        If find minimum absolute difference between three sum and target by Brute-Force, time complexity will be O(n^3)
        If first sort numbers, e.g. quick sort whose time complexity is O(n), and then use two pointers to denote the
        second and third number whose time complexity will be O(n^2). The overall time complexity will therefore be O(n^2)
        :param numbers:
        :param target:
        :return:
        """
        numbers.sort()
        closest_3sum = None
        for i in range(len(numbers)):
            left, right = i+1, len(numbers)-1
            while left < right:
                sum_tmp = numbers[i]+numbers[left]+numbers[right]
                if closest_3sum is None or abs(sum_tmp-target) < abs(closest_3sum-target):
                    closest_3sum = sum_tmp
                if sum_tmp <= target:
                    left += 1
                else:
                    right -= 1
        return closest_3sum

s = Solution()
print(s.three_sum_closest([2, 1, 4, 5, 6, 0], 5.5))
