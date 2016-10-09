class Solution(object):
    def majority_number_III(self, nums, k):
        candidate_count_dict = {}
        for num in nums:
            if candidate_count_dict.get(num, None) is not None:
                candidate_count_dict[num] += 1
            elif len(candidate_count_dict) < k-1:
                candidate_count_dict[num] = 1
            else:
                for c in list(candidate_count_dict.keys()):
                    candidate_count_dict[c] -= 1
                    if candidate_count_dict[c] == 0:
                        candidate_count_dict.pop(c)
        candidate_count_dict = dict.fromkeys(candidate_count_dict, 0)
        candidate = count = 0
        for num in nums:
            if candidate_count_dict.get(num, None) is not None:
                candidate_count_dict[num] += 1
                if candidate_count_dict[num] > count:
                    count = candidate_count_dict[num]
                    candidate = num
        return candidate

s = Solution()
print(s.majority_number_III([7,1,7,7,61,61,61,10,10,10,61], 3))