from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n = len(gas)
        for i in range(n):
            gas[i] -= cost[i]
        def check(gas_idx):
            cur_gas = 0
            for i in range(gas_idx,n+gas_idx):
                cur_gas+=gas[i%n]
                if cur_gas<0:
                    return False
            return True
        # 从0#加油站出发，到达对应的加油站时剩余的油量
        prefixes = [0]*(n+1)
        min_gas = 0
        min_idx = -1
        for i in range(1,n+1):
            prefixes[i]=prefixes[i-1]+gas[i-1]
            if prefixes[i]<min_gas:
                min_gas = prefixes[i]
                min_idx = i
        return min_idx if check(min_idx) else -1

if __name__ == '__main__':
    sol = Solution()
    # print(sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    print(sol.canCompleteCircuit(gas = [3,1,1], cost = [1,1,2]))