class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        # 初始化dp
        # t[n:](空串)是任意字符串的子串
        for i in range(m+1):
            dp[i][n] = 1
        # s[i:]i<n不是空串，不是任意非空字符串的子串
        for j in range(n):
            dp[m][j] = 0
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                # s[i:]一定包括s[i+1:]的所有子串
                dp[i][j] = dp[i+1][j]
                # 如果新加入的字符都相同，那么还需要加入原本没加字符的情况
                if s[i]==t[j]:
                    dp[i][j]+=dp[i+1][j+1]
        return dp[0][0]
if __name__ == '__main__':
    sol = Solution()
    print(sol.numDistinct(s = "rabbbit", t = "rabbit"))
    print(sol.numDistinct(s = "babgbag", t = "bag"))