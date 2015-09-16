__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        print(nums1, nums2)
        n1, n2 = len(nums1), len(nums2)
        m1, m2 = n1//2, n2//2
        if n1 == 0:
            if n2 == 0:
                return None
            if n2 % 2 == 0:
                return (nums2[m2-1]+nums2[m2])/2.0
            else:
                return nums2[m2]
        if n2 == 0:
            if n1 % 2 == 0:
                return (nums1[m1-1]+nums1[m1])/2.0
            else:
                return nums1[m1]
        if n1 == 1:
            if n2 == 1:
                return (nums1[0]+nums2[0])/2.0
            if n2 % 2 == 0:
                if nums1[0] >= nums2[m2]:
                    return nums2[m2]
                if nums1[0] <= nums2[m2-1]:
                    return nums2[m2-1]
                else:
                    return nums1[0]
            else:
                if nums1[0] >= nums2[m2+1]:
                    return (nums2[m2]+nums2[m2+1])/2.0
                if nums1[0] <= nums2[m2-1]:
                    return (nums2[m2-1]+nums2[m2])/2.0
                else:
                    return (nums1[0]+nums2[m2])/2.0
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
                    return (nums1[m1]+nums1[m1+1])/2.0
                if nums2[0] <= nums1[m1-1]:
                    return (nums1[m1-1]+nums1[m1])/2.0
                else:
                    return (nums2[0]+nums1[m1])/2.0
        elif n1 == 2:
            if n2 == 2:
                num12 = sorted(nums1+nums2)
                return (num12[1]+num12[2])/2.0
            elif n2 % 2 == 0:
                num12 = sorted(nums1+nums2)
                return (num12[(n2+2)//2-1]+num12[(n2+2)//2])/2.0
            else:
                num12 = sorted(nums1+nums2)
                return num12[(n2+2)//2]
        elif n2 == 2:
            if n1 % 2 == 0:
                num12 = sorted(nums1+nums2)
                return (num12[(n1+2)//2-1]+num12[(n1+2)//2])/2.0
            else:
                num12 = sorted(nums1+nums2)
                return num12[(n1+2)//2]
        else:
            if n1 % 2 == 0 and n2 % 2 == 0:
                if (nums1[m1-1]+nums1[m1]) < (nums2[m2-1]+nums2[m2]):
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[m1-1:], nums2[:n2-m1+1])
                    else:
                        return self.findMedianSortedArrays(nums1[m2-1:], nums2[:m2+1])
                else:
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[:m1+1], nums2[m1-1:])
                    else:
                        return self.findMedianSortedArrays(nums1[:n1-m2+1], nums2[m2-1:])
            elif n1 % 2 != 0 and n2 % 2 != 0:
                if nums1[m1] < nums2[m2]:
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[m1:], nums2[:n2-m1])
                    else:
                        return self.findMedianSortedArrays(nums1[m2:], nums2[:m2+1])
                else:
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[:m1+1], nums2[m1:])
                    else:
                        return self.findMedianSortedArrays(nums1[:n1-m2], nums2[m2:])
            elif n1 % 2 == 0 and n2 % 2 != 0:
                if (nums1[m1-1]+nums1[m1])/2.0 < nums2[m2]:
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[m1-1:], nums2[:n2-m1+1])
                    else:
                        return self.findMedianSortedArrays(nums1[m2:], nums2[:m2+1])
                elif (nums1[m1-1]+nums1[m1])/2.0 > nums2[m2]:
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[:m1+1], nums2[m1-1:])
                    else:
                        return self.findMedianSortedArrays(nums1[:n1-m2], nums2[m2:])
                else:
                    return nums2[m2]
            elif n1 % 2 != 0 and n2 % 2 == 0:
                if nums1[m1] < (nums2[m2-1]+nums2[m2])/2.0:
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[m1:], nums2[:n2-m1])
                    else:
                        return self.findMedianSortedArrays(nums1[m1:], nums2[:n2-m1])
                elif nums1[m1] > (nums2[m2-1]+nums2[m2])/2.0:
                    if n1 <= n2:
                        return self.findMedianSortedArrays(nums1[:m1+1], nums2[m1:])
                    else:
                        return self.findMedianSortedArrays(nums1[:n1-m2+1], nums2[m2-1:])
                else:
                    return nums1[m1]

    def find_median_sorted_arrays_kth_min(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1+n2 & 1:
            return find_kth_smallest(nums1, n1, nums2, n2, (n1+n2)//2+1)
        else:
            return (find_kth_smallest(nums1, n1, nums2, n2, (n1+n2)//2)+\
                    find_kth_smallest(nums1, n1, nums2, n2, (n1+n2)//2+1))/2.0

def find_kth_smallest(nums1, n1, nums2, n2, k):
    if n1 > n2:
        return find_kth_smallest(nums2, n2, nums1, n1, k)
    if n1 == 0:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0], nums2[0])
    i = min(k//2, n1)
    j = k-i
    if nums1[i-1] < nums2[j-1]:
        return find_kth_smallest(nums1[i:], n1-i, nums2, n2, k-i)
    elif nums1[i-1] > nums2[j-1]:
        return find_kth_smallest(nums1, n1, nums2[j:], n2-j, k-j)
    else:
        return nums1[i-1]

s = Solution()
m1 = s.findMedianSortedArrays([], [])
m2 = s.find_median_sorted_arrays_kth_min([], [2, 3])
print(m1, m2)
