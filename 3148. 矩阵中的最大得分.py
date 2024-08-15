class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_val = [[float('inf') for __ in range(n+1)] for _ in range(m+1)]
        ans = -float('inf')
        for i in range(1,m+1):
            for j in range(1,n+1):
                ans = max(ans, grid[i-1][j-1]-min(min_val[i-1][j], min_val[i][j-1]))
                min_val[i][j] = min(grid[i-1][j-1], min_val[i-1][j], min_val[i][j-1])
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScore(grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]))