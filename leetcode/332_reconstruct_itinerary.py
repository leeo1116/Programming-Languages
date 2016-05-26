class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from_to_dict = {}
        tickets_len = len(tickets)
        for ticket in tickets:
            if from_to_dict.get(ticket[0], None):
                # Insertion sort
                i = len(from_to_dict[ticket[0]])-1
                while i > -1 and ticket[1] > from_to_dict[ticket[0]][i]:
                    i -= 1
                # Insert at i+1
                from_to_dict[ticket[0]] = from_to_dict[ticket[0]][:i+1]+[ticket[1]]+from_to_dict[ticket[0]][i+1:]
            else:
                from_to_dict[ticket[0]] = [ticket[1]]

        iti_list = ["JFK"]*(tickets_len+1)
        for i in range(1, tickets_len+1):
            first_dest = from_to_dict[iti_list[i-1]][-1]
            temp = ""
            if from_to_dict.get(first_dest, None) or i == tickets_len:
                iti_list[i] = from_to_dict[iti_list[i-1]].pop()
            else:
                temp = from_to_dict[iti_list[i-1]].pop()
                iti_list[i] = from_to_dict[iti_list[i - 1]].pop()
                from_to_dict[iti_list[i-1]].append(temp)

        return iti_list


s = Solution()
print(s.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))



