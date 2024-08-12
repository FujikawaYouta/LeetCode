class Solution:
    # def lengthOfLIS(self, nums: list[int]) -> int:
    #     n = len(nums)
    #     max_len = 1
    #     dp = [1 for _ in nums]
    #     for i in range(1, n):
    #         cur_value = 0
    #         for j in range(i):
    #             if nums[j]<nums[i]:
    #                 cur_value = max(cur_value, dp[j])
    #         dp[i] = cur_value+1
    #         max_len = max(max_len, dp[i])
    #     return max_len
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i]表示nums[i]结尾的最大递增子序列
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
if __name__ == '__main__':
    sol=Solution()
    print(sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLIS(nums = [0,1,0,3,2,3]))
    print(sol.lengthOfLIS(nums = [1,3,6,7,9,4,10,5,6]))