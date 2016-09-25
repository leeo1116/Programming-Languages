class Solution(object):
    def can_complete_circle(self, gas, cost):
        gas_tank, station_num, gas_cost_balance, start_index = 0, len(gas), 0, 0
        for i in range(station_num):
            gas_tank += (gas[i]-cost[i])
            if gas_tank < 0:
                start_index = (i+1) % station_num
                gas_tank = 0
            gas_cost_balance += (gas[i]-cost[i])
        return start_index if gas_cost_balance >= 0 else -1

s = Solution()
print(s.can_complete_circle([2,0,1,2,3,4,0], [0,1,0,0,0,0,11]))


