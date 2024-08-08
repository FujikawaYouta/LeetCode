class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # 考虑i<j的情况
        # 如果s[i]=s[j]，那么dp[i][j]=dp[i+1][j-1]+2
        # 如果s[i]!=s[j]，那么dp[i][j]继承dp[i+1][j]和dp[i][j]中较大的值
        for i in range(n):
            for j in range(i+1,n):
                left = j-i-1
                right = j
                if s[left]==s[right]:
                    dp[left][right]=dp[left+1][right-1]+2
                else:
                    dp[left][right]=max(dp[left+1][right],dp[left][right-1])
        return dp[0][n-1]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindromeSubseq(s="bbbab"))