import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from_to_dict = {}  # or use collections.defaultdict(list)
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

        iti_list = []

        def visit(city_from):
            while from_to_dict.get(city_from, None):
                visit(from_to_dict[city_from].pop())
            iti_list.append(city_from)

        visit("JFK")
        return iti_list[::-1]

s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(s.findItinerary(tickets))


# def func():
#     a = [0]
#
#     def swim():
#         # a.append(3)
#         a = [1]+a
#         return a
#     return swim()
#
# print(func())
#
