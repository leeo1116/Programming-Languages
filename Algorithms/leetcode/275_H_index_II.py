class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations_len = len(citations)
        left, right = 0, citations_len-1
        while left <= right:
            mid = left+(right-left)//2
            if citations[mid] == citations_len-mid:
                return citations[mid]
            elif citations[mid] > citations_len-mid:
                right = mid-1
            else:
                left = mid+1
        return citations_len-left
