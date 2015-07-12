__author__ = 'Liang Li'

class Solution:
    # @return an integer
    def longest_substring(self, s):
        i = j = max_len = 0
        s_hash = {}
        for char in s:
            if s_hash.get(char, None) is not None and s_hash.get(char) >= i:
                i = s_hash[char]+1
            s_hash[char] = j  # s_hash table for all characters in s (overwrite duplicated key-value)
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len

class Solution_x:
    def longest_substring(self, s):
        i = max_len = 0
        counts = [-1]*256
        for j in range(len(s)):
            if counts[ord(s[j])] >= i:
                i = counts[ord(s[j])] + 1
            counts[ord(s[j])] = j
            max_len = max(max_len, j-i+1)
        return max_len

s1 = Solution()
length = s1.longest_substring("abba")
print(length)
