class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i][0]是非负数最大值
        # dp[i][1]是负数最大值
        dp = [[-1,1] for _ in range(n)]
        for i in range(n):
            if nums[i]>=0:
                dp[i][0]=nums[i]
        for i in range(n):
            if nums[i]<0:
                dp[i][1]=nums[i]
        for i in range(1,n):
            if nums[i]>=0:
                dp[i][0]=max(dp[i][0],dp[i-1][0]*nums[i])
                dp[i][1]=min(dp[i][1],dp[i-1][1]*nums[i])
            else:
                dp[i][0]=max(dp[i][0],dp[i-1][1]*nums[i])
                dp[i][1]=min(dp[i][1],dp[i-1][0]*nums[i])
            dp[i][0]=max(dp[i][0],dp[i-1][0])
            dp[i][1]=min(dp[i][1],dp[i-1][1])
        if dp[n-1][0]<0:
            return dp[n-1][1]
        if dp[n-1][1]>0:
            return dp[n-1][0]
        return max(dp[n-1][0],dp[n-1][1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxStrength(nums = [9,6,3]))