class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.palindrome_partition_list(s)

    def palindrome_partition_list(self, s):
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s[0]]]
        p_list = []
        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                if i == len(s)-1:
                    p_list.append([s[:i+1]])
                    break
                for p in self.palindrome_partition_list(s[i+1:]):
                    p_list.append([s[:i+1]]+p)
        return p_list


    def is_palindrome(self, s):
        if not s:
            return False
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return i > j


s = Solution()
print(s.partition("aba"))