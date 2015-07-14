__author__ = 'Liang Li'
class Solution_x:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        totlen = len(A) + len(B)
        if (1 & totlen):
            return self.findK(A, B, (totlen + 1) / 2)
        else:
            return (self.findK(A, B, totlen / 2) + self.findK(A, B, totlen / 2 + 1)) / 2.0

    def findK(self, A, B, K):
        la, lb, pa, pb = len(A), len(B), min(K/2, len(A)), K - min(K/2, len(A))
        if (la > lb):
            return self.findK(B, A, K)
        if (la == 0):
            return B[K-1]
        if (K == 1):
            return min(A[0], B[0])
        if A[pa - 1] < B[pb - 1]:
            return self.findK(A[pa:], B, K - pa)
        elif A[pa - 1] > B[pb - 1]:
            return self.findK(A, B[pb:], K- pb)
        else:
            return A[pa - 1]

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def median_of_two_sorted_array(self, nums1, nums2):
        # print(nums1, nums2)
        n1, n2 = len(nums1), len(nums2)
        m1, m2 = n1//2, n2//2
        if n1 == 1:
            if n2 == 1:
                return (nums1[0]+nums2[0])/2
            if n2 % 2 == 0:
                if nums1[0] >= nums2[m2]:
                    return nums2[m2]
                if nums1[0] <= nums2[m2-1]:
                    return nums2[m2-1]
                else:
                    return nums1[0]
            else:
                if nums1[0] >= nums2[m2+1]:
                    return (nums2[m2]+nums2[m2+1])/2
                if nums1[0] <= nums2[m2-1]:
                    return (nums2[m2-1]+nums2[m2])/2
                else:
                    return (nums1[0]+nums2[m2])/2
        elif n2 == 1:
            if n1 % 2 == 0:
                if nums2[0] >= nums1[m1]:
                    return nums1[m1]
                if nums2[0] <= nums1[m1-1]:
                    return nums1[m1-1]
                else:
                    return nums2[0]
            else:
                if nums2[0] >= nums1[m1+1]:
                    return (nums1[m1]+nums1[m1+1])/2
                if nums2[0] <= nums1[m1-1]:
                    return (nums1[m1-1]+nums1[m1])/2
                else:
                    return (nums2[0]+nums1[m1])/2
        elif n1 == 2:
            if n2 == 2:
                num12 = sorted(nums1+nums2)
                return (num12[1]+num12[2])/2
            #elif n2 % 2 == 0:
        else:
            if n1 % 2 == 0 and n2 % 2 == 0:
                if (nums1[m1-1]+nums1[m1]) < (nums2[m2-1]+nums2[m2]):
                    return self.median_of_two_sorted_array(nums1[m1:], nums2[:m2])
                else:
                    return self.median_of_two_sorted_array(nums1[:m1], nums2[m2:])
            elif n1 % 2 != 0 and n2 % 2 != 0:
                if nums1[m1] < nums2[m2]:
                    return self.median_of_two_sorted_array(nums1[m1:], nums2[:m2+1])
                else:
                    return self.median_of_two_sorted_array(nums1[:m1+1], nums2[m2:])
            elif n1 % 2 == 0 and n2 % 2 != 0:
                if (nums1[m1-1]+nums1[m1])/2 < nums2[m2]:
                    return self.median_of_two_sorted_array(nums1[m1:], nums2[:m2+1])
                else:
                    return self.median_of_two_sorted_array(nums1[:m1+1], nums2[m2:])
            elif n1 % 2 != 0 and n2 % 2 == 0:
                if nums1[m1] < (nums2[m2-1]+nums2[m2])/2:
                    return self.median_of_two_sorted_array(nums1[m1:], nums2[:m2])
                else:
                    return self.median_of_two_sorted_array(nums1[:m1], nums2[m2:])



s = Solution()
m = s.median_of_two_sorted_array([3, 8], [4, 5, 6, 7])
print(m)
s_x = Solution_x()
m_x = s_x.findMedianSortedArrays([3, 8], [4, 5, 6, 7])
print(m)