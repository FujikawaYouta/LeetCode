class Solution:
    def minRectanglesToCoverPoints(self, points: list[list[int]], w: int) -> int:
        points = sorted(list({point[0] for point in points}))
        n = len(points)
        left_pt = points[0]
        right_pt = points[-1]
        cnt = 0
        cur_ptr = 0
        while left_pt<=right_pt:
            cnt+=1
            left_pt+=w
            while cur_ptr<n and left_pt>=points[cur_ptr]:
                cur_ptr+=1
            if cur_ptr==n:
                break
            left_pt=points[cur_ptr]
        return cnt

if __name__ == '__main__':
    sol = Solution()
    print(sol.minRectanglesToCoverPoints(points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1))
    print(sol.minRectanglesToCoverPoints(points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2))