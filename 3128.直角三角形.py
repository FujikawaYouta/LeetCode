class Solution:
    def numberOfRightTriangles(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # 对于每一行，有多少个1
        one_count_row = [sum(row) for row in grid]
        one_count_col = [0 for _ in range(m)]
        # 对于每一列，有多少个1
        for j in range(m):
            for i in range(n):
                one_count_col[j]+=grid[i][j]
        # 对于每一个元素作为直角点，
        # 他构成的三角形个数为(r-1)*(c-1)
        # r, c分别是当前行和当前列的1的个数
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and one_count_col[j]>1 and one_count_row[i]>1:
                    ans += (one_count_col[j]-1) * (one_count_row[i]-1)
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfRightTriangles(grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]))