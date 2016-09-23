class Solution(object):
    def wood_cut(self, L, k):
        maxLi = max(L) if L else 0
        left, right = 0, maxLi
        while left <= right:
            mid = left+(right-left)//2
            if self.do_cut(L, k, mid):
                left = mid+1
            else:
                right = mid-1
        return right

    @staticmethod
    def do_cut(L, k, tmp):
        if tmp == 0:
            return True
        num = 0
        for l in L:
            num += l//tmp
        return num >= k


s = Solution()
print(s.wood_cut([], 7))