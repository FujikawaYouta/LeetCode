class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        dp = [1]*n
        for i in range(1,n):
            if ord(s[i])-ord(s[i-1])==1:
                dp[i]=dp[i-1]+1
                ans = max(ans, dp[i])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestContinuousSubstring(s = "abcde"))