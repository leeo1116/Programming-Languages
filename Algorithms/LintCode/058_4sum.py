class Solution(object):
    def four_sum(self, numbers, target):
        numbers.sort()
        quadruplets_list = []
        for i in range(len(numbers) - 3):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, len(numbers) - 2):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                left, right = j + 1, len(numbers) - 1
                while left < right:
                    four_sum_tmp = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    if four_sum_tmp == target:
                        quadruplets_list.append((numbers[i], numbers[j], numbers[left], numbers[right]))
                        left += 1
                        right -= 1
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1
                    elif four_sum_tmp < target:
                        left += 1
                    elif four_sum_tmp > target:
                        right -= 1
        return quadruplets_list

s = Solution()
print(s.four_sum([1, 2, 3], 5))

