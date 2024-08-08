class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j]代表word1[:i]到word2[:j]需要的最少操作次数
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        # 初始化dp：一个空字符串到任何一个长为n的字符串需要n次
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        # 对于每一个项dp[i][j]，取插入一个字符，删除一个字符，替换一个字符的最小值
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
        return dp[m][n]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance(word1 = "horse", word2 = "ros"))