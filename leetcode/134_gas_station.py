class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas_sum, cost_sum, tank, start = 0, 0, 0, 0
        for i in range(len(gas)):
            gas_sum += gas[i]
            cost_sum += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:  # gas at station i < cost driving from i to i+1, it is the necessary but not sufficient
                          # condition of tank < 0
                start = i+1
                tank = 0
        if gas_sum < cost_sum:
            return -1
        else:
            return start