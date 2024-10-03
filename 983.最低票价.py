class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        # 表示覆盖到第i天需要的最小金额
        dp = [0]*(days[-1]+1)
        last_day = days[0]
        for day in days:
            for i in range(last_day+1,day):
                dp[i]=dp[last_day]
            last_day = day
            # 买一日票
            dp[day]=dp[day-1]+costs[0]
            idx1 = max(day-7,0)
            dp[day]=min(dp[day], dp[idx1]+costs[1])
            idx2 = max(day-30,0)
            dp[day]=min(dp[day], dp[idx2]+costs[2])
        return dp[-1]
    
if __name__ == '__main__':
    sol = Solution()
    # print(sol.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
    print(sol.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))