class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        i = j = 0
        while i < len(v1_list) and j < len(v2_list):
            if int(v1_list[i]) > int(v2_list[j]):
                return 1
            elif int(v1_list[i]) < int(v2_list[j]):
                return -1
            else:
                i += 1
                j += 1
                continue

        if i != len(v1_list) and j == len(v2_list):
            return 1
        elif i == len(v1_list) and j != len(v2_list):
            return -1
        elif i == len(v1_list) and j == len(v2_list):
            return 0
        else:
            print("Never print this")



s = Solution()
print(s.compareVersion("1", "1.1"))