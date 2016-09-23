class Solution(object):
    def search(self, A, target):
        left, right = 0, len(A)-1
        while left <= right:
            mid = left+(right-left)//2
            if A[mid] == target:
                return True
            elif A[mid] >= A[left]:
                if A[mid] > target >= A[left]:
                    right = mid
                else:
                    left = mid+1
            elif A[mid] <= A[left]:
                if A[mid] < target <= A[right]:
                    left = mid+1
                else:
                    right = mid
            else:
                right -= 1
        return False

s = Solution()
print(s.search([2,2,2,3,1], 1))