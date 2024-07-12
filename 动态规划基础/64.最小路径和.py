class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 记录到每一个格子的最小代价，外围用0填充
        dp = [[float('inf') for _ in range(n+1)] for __ in range(m+1)]
        dp[1][1] = grid[0][0]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    continue
                dp[i][j]=grid[i-1][j-1]+min(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
    
if __name__=='__main__':
    sol = Solution()
    print(sol.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))