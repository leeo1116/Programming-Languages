__doc__ = """
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The
overall run time complexity should be O(log (m+n)).
 """


class Solution():
    def __init__(self, index):
        self.index = index

    def median_of_two_sorted_array(self, nums1, nums2):
        """
        Find the median of two sorted arrays in ascending order
        :param nums1: array1
        :param nums2: array2
        :return m: median of array1 and array2
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1+len2) & 1:
            return find_kth_smallest(nums1, nums2, (len1+len2)//2+1)
        else:
            return (find_kth_smallest(nums1, nums2, (len1+len2)//2) +
                    find_kth_smallest(nums1, nums2, (len1+len2)//2+1))/2


def find_kth_smallest(nums1, nums2, k):
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 > len2:
        return find_kth_smallest(nums2, nums1, k)
    if len1 == 0:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0], nums2[0])
    i = min(k//2, len1)
    j = k-i
    if nums1[i-1] < nums2[j-1]:
        return find_kth_smallest(nums1[i:], nums2, k-i)
    elif nums1[i-1] > nums2[j-1]:
        return find_kth_smallest(nums1, nums2[j:], k-j)
    else:
        return nums1[i-1]


s = Solution(4)
print(s.median_of_two_sorted_array([], [2, 3]))
