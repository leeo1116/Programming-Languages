class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        citations_len = len(citations)
        citation_list = [0]*(citations_len+1)
        h_index = 0

        # Bucket sort
        for i in range(citations_len):
            if citations[i] > citations_len:
                citation_list[citations_len] += 1
            else:
                citation_list[citations[i]] += 1

        # Use index of citation_list to denote the citations
        for i in range(citations_len, -1, -1):
            h_index += citation_list[i]
            if h_index >= i:
                return i
        return 0


