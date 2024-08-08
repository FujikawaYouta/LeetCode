class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        # dp[i][j]表示s1[:i]到s2[:j]需要的最小ascii和
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0]+ord(s1[i-1])
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1]+ord(s2[j-1])
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        return dp
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumDeleteSum(s1 = "delete", s2 = "leet"))