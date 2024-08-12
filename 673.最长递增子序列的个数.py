class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i]表示以nums[i]结尾的，长度为j的子序列的个数
        dp = [1 for _ in range(n)]
        dp_max = 0
        cnt = [1 for _ in range(n)]
        ans = 0
        for i in range(n):
            max_len = 0
            for j in range(i):
                if nums[i]>nums[j]:
                    if max_len<dp[j]:
                        max_len = dp[j]
                        cnt[i]=cnt[j]
                    elif max_len==dp[j]:
                        cnt[i]+=cnt[j]
            dp[i] = max_len+1
            if dp_max<dp[i]:
                dp_max = dp[i]
                ans = cnt[i]
            elif dp_max==dp[i]:
                ans += cnt[i]
        return ans
    
if __name__ == '__main__':
    sol=Solution()
    print(sol.findNumberOfLIS(nums = [1,3,5,4,7]))
    print(sol.findNumberOfLIS(nums = [1,2,4,3,5,4,7,2]))
    # 12357
    # 12457
    # 12347