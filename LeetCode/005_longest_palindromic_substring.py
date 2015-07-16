__author__ = 'liangl2'
class Solution:
    # @param {string} s
    # @return {string}
    def longest_palindrome(self, s):
        ss = '#'.join("*{}%".format(s))
        ss_len = len(ss)
        P = [0]*ss_len
        id = mx = 0
        for i in range(1, ss_len-1):
            P[i] = (mx > i)*min(mx-i, P[2*id-i])
            while ss[i+1+P[i]] == ss[i-1-P[i]]:
                P[i] += 1
            if i+P[i] > mx:
                id, mx = i, i+P[i]

        max_p, index = max((n, i) for i, n in enumerate(P))
        return s[(index-max_p)//2:(index+max_p)//2]

s = Solution()
p = s.longest_palindrome("afdabcdeeafadafaeedcbaelhssf")
print(p)


