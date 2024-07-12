class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        dp = [[col_row for col_row in row] for row in triangle]
        for i in range(m):
            for j in range(i+1):
                if i == 0:
                    continue
                elif j==0:
                    dp[i][j] += dp[i-1][j]
                elif j==i:
                    dp[i][j] += dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j]+min(dp[i-1][j], dp[i-1][j-1])
        return min(dp[m-1])
    
if __name__=='__main__':
    sol = Solution()
    print(sol.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))