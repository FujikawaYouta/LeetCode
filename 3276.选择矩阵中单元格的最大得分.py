class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_map = map(max,grid)
        max_val = max(max_map)
        pos = [set() for _ in range(max_val+1)]
        # visited_rows表示已经访问过的行序号集合
        # def dfs(i,visited_rows):
        # j表示已访问的行序号集合
        def dfs(i,j):
            if i==0:
                return 0
            ans = dfs(i-1,j)
            # 选i 或者 不选i
            # for row in range(m):
            for row in pos[i]:
                # if row not in visited_rows and i in grid[row]:
                # if (1<<row)&j==0 and i in grid[row]:
                if (1<<row)&j==0:
                    ans = max(ans, i+dfs(i-1,j | (1<<row)))
            return ans
        
        for i,row in enumerate(grid):
            for val in row:
                pos[val].add(i)
        # visited_rows=set()
        # return dfs(max_val, visited_rows)
        j = 0
        return dfs(max_val, j)
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScore([[67,67,11,60,7],[11,67,53,60,60],[11,21,13,7,53],[40,60,67,7,11],[44,57,11,40,11],[40,55,84,43,11],[13,84,15,58,1],[31,1,15,60,45],[75,53,15,18,7]]))
    print(sol.maxScore([[8,7,6],[8,3,2]]))