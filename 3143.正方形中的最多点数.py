class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        # 其实取坐标点的绝对值的最大值就可以
        n = len(points)
        points = [max(abs(point[0]), abs(point[1])) for point in points]
        sorted_s = [c for _, c in sorted(zip(points, s))]
        points = sorted(points)
        visited_points = set()
        cur_len = points[0]
        ans = 0
        temp_ans = 0
        for i in range(n):
            if points[i]!=cur_len:
                ans+=temp_ans
                temp_ans=0
            # 这个没见过，可以添加
            if sorted_s[i] not in visited_points:
                visited_points.add(sorted_s[i])
                temp_ans+=1
            # 这个见过，不可以添加
            else:
                temp_ans=0
                break
            cur_len = points[i]
        return ans+temp_ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPointsInsideSquare(points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"))
    print(sol.maxPointsInsideSquare(points = [[1,1],[-2,-2],[-2,2]], s = "abb"))
    print(sol.maxPointsInsideSquare(points = [[1,1],[-1,-1],[2,-2]], s = "ccd"))
    print(sol.maxPointsInsideSquare(points = [[1,1]], s = "a"))