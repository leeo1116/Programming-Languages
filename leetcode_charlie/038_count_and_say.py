class Solution(object):
    def count_and_say(self, n):
        """
        :type n: int
        :rtype: str
        """
        current_num_str = '1'
        while n-1:
            next_num_str = self.count(current_num_str)
            current_num_str = next_num_str
            n -= 1
        return current_num_str

    def count(self, num_str):
        new_num_str = ''
        num_str_len = len(num_str)
        i = 0
        while i < num_str_len:
            j = 0
            while i+j < num_str_len and num_str[i+j] == num_str[i]:
                j += 1
            new_num_str = new_num_str+str(j)+num_str[i]
            i += j
        return new_num_str


s = Solution()
print(s.count_and_say(10))