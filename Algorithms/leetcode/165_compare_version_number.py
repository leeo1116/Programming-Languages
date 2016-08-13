class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        v1_list_len = len(v1_list)
        v2_list_len = len(v2_list)
        max_len = max(v1_list_len, v2_list_len)
        for i in range(max_len):
            v1 = int(v1_list[i]) if i < v1_list_len else 0
            v2 = int(v2_list[i]) if i < v2_list_len else 0
            if v1 != v2:
                return 1-2*(v2 > v1)
        return 0

s = Solution()
print(s.compareVersion("1", "1.0.1"))