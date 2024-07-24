class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 1
        dp = [1 for _ in nums]
        for i in range(1, n):
            cur_value = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    cur_value = max(cur_value, dp[j])
            dp[i] = cur_value+1
            max_len = max(max_len, dp[i])
        return max_len
    
if __name__ == '__main__':
    sol=Solution()
    print(sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLIS(nums = [1,3,6,7,9,4,10,5,6]))