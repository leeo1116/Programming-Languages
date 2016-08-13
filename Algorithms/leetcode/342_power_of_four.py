class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # check single '1' bit: num-1 make the lowest '1' bit be '0' bit, and if there are no higher bits equal to '1',
        # then num & (num-1) = 0
        return num > 0 and (num & (num-1)) == 0 and (num-1) % 3 == 0
        # return num > 0 and (num & (num-1)) == 0 and (num & 0x55555555) != 0
