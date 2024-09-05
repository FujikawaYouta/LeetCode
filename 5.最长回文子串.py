# 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans=s[0]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                if len(ans)==1:
                    ans=s[i:i+2]
        for k in range(2,n):
            for i in range(n-k):
                if dp[i+1][k+i-1]==True and s[i]==s[k+i]:
                    dp[i][k+i]=True
                    if len(ans)!=k+1:
                        ans=s[i:i+k+1]
        return ans
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome(s = "ccc"))