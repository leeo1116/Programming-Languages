class Solution(object):
    def two_sum(self, numbers, target):
        num_index_map = {}
        for i, num in enumerate(numbers):
            if num_index_map.get(target-num, None) is not None:
                return [num_index_map[target-num]+1, i+1]
            else:
                num_index_map[num] = i
        return []