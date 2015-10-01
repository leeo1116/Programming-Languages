__author__ = 'liangl2'
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        i = 0
        ans = []

        # sliding window(s)
        for k in range(l):
            left = k
            sub_dict = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                test_word = s[j:j+l]
                # valid word
                if test_word in d:
                    if test_word in sub_dict:
                        sub_dict[test_word] += 1
                    else:
                        sub_dict[test_word] = 1
                    count += 1
                    while sub_dict[test_word] > d[test_word]:
                        sub_dict[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    sub_dict = {}
                    count = 0
        return ans

s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))