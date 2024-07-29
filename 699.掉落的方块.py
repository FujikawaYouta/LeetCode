class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        n = len(positions)
        cur_height = [0 for _ in range(n)]
        max_height = [0 for _ in range(n)]
        max_height[0] = positions[0][1]
        for i in range(n):
            cur_height[i]=positions[i][1]
            for j in range(i):
                if positions[j][0]+positions[j][1]>positions[i][0] and \
                    positions[j][0]<positions[i][0]+positions[i][1]:
                    cur_height[i] = max(positions[i][1]+cur_height[j], cur_height[i])
            if i>0:
                max_height[i] = max(max_height[i-1], cur_height[i])
        return max_height
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.fallingSquares(positions=[[1,2],[2,3],[6,1]]))