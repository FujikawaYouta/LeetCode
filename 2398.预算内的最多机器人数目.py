# 单调队列可以用来解决动态最值问题，学会了
class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        n = len(chargeTimes)
        l_ptr = 0
        max_ans = 0
        run_sum = 0
        max_charge = 0
        charge_cost = []
        for i in range(n):
            # 维护单调递减队列
            while charge_cost and chargeTimes[charge_cost[-1]]<=chargeTimes[i]:
                charge_cost.pop()
            charge_cost.append(i)
            run_sum+=runningCosts[i]
            # 判断是否符合条件，如果不符合，右移左指针缩小窗口
            while l_ptr<i and chargeTimes[charge_cost[0]]+(i-l_ptr+1)*run_sum>budget:
                run_sum-=runningCosts[l_ptr]
                if charge_cost[0]==l_ptr:
                    charge_cost.pop(0)
                l_ptr+=1
            if len(charge_cost) and chargeTimes[charge_cost[0]]+(i-l_ptr+1)*run_sum<=budget:
                max_ans = max(max_ans,i-l_ptr+1)
        return max_ans
    
if __name__ == '__main__':
    sol = Solution()
    # print(sol.maximumRobots(chargeTimes = [8,17,5,2], runningCosts=[1,14,4,1], budget=19))
    print(sol.maximumRobots(chargeTimes = [11,12,19], runningCosts=[10,8,7], budget=19))