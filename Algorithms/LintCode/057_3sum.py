class Solution(object):
    def three_sum(self, numbers):
        numbers.sort()
        triplets = set()
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                if numbers[i] + numbers[left] + numbers[right] == 0:
                    triplets.add((numbers[i], numbers[left], numbers[right]))
                    left += 1
                    right -= 1
                elif numbers[i] + numbers[left] + numbers[right] < 0:
                    left += 1
                elif numbers[i] + numbers[left] + numbers[right] > 0:
                    right -= 1
        return list(triplets)

s = Solution()
print(s.three_sum([-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5]))
