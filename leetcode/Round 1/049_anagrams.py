__author__ = 'liangl2'
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        str_hash = {}
        anagrams = []
        for i in range(len(strs)):
            if str_hash.get(''.join(sorted(strs[i])), None):
                str_hash[''.join(sorted(strs[i]))].append(i)
            else:
                str_hash[''.join(sorted(strs[i]))] = [i]

        for k, v in str_hash.items():
            if len(v) > 1:
                for i in range(len(v)):
                    anagrams.append(strs[v[i]])

        return anagrams

s = Solution()
print(s.anagrams(["abc", "cba", "ad", "dac"]))

