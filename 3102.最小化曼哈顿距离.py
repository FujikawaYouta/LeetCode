from sortedcontainers import SortedList
class Solution:
    # def minimumDistance(self, points: list[list[int]]) -> int:
    #     def manhattenDistance(point_x, point_y):
    #         return abs(point_x[0]-point_y[0])+\
    #             abs(point_x[1]-point_y[1])
    #     n = len(points)
    #     # distance = [[0 for _ in range(n)] for __ in range(n)]
    #     point_farthest = []
    #     for i, src_point in enumerate(points):
    #         farthest = [0, 0]
    #         for j in range(n):
    #             dst_point = points[j]
    #             cur_distance = manhattenDistance(src_point, dst_point)
    #             # distance[i][j] = cur_distance
    #             if cur_distance>farthest[1]:
    #                 farthest[1] = cur_distance
    #                 if farthest[1]>farthest[0]:
    #                     tmp = farthest[0]
    #                     farthest[0] = farthest[1]
    #                     farthest[1] = tmp
    #         point_farthest.append(farthest)
    #     # 跳过对应的点，找到最远点的最小值
    #     min_of_max_value = float('inf')
    #     for i, point in enumerate(points):
    #         # 对于某个点
    #         cur_max_distance = 0
    #         for j in range(n):
    #             if i==j:
    #                 continue
    #             # cur_distance = distance[i][j]
    #             cur_distance = manhattenDistance(point, points[j])
    #             # 当前距离如果是最远，就选择第二远的
    #             if cur_distance == point_farthest[j][0]:
    #                 cur_max_distance = max(cur_max_distance, point_farthest[j][1])
    #             else:
    #                 cur_max_distance = max(cur_max_distance, point_farthest[j][0])
    #         min_of_max_value = min(min_of_max_value, cur_max_distance)
    #     return min_of_max_value
    def minimumDistance(self, points: list[list[int]]) -> int:
        sx = SortedList(p[0] - p[1] for p in points)
        sy = SortedList(p[0] + p[1] for p in points)
        res = float('inf')
        for p in points:
            sx.remove(p[0] - p[1])
            sy.remove(p[0] + p[1])
            res = min(res, max(sx[-1] - sx[0], sy[-1] - sy[0]))
            sx.add(p[0] - p[1])
            sy.add(p[0] + p[1])
        return res
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumDistance(points = [[3,10],[5,15],[10,2],[4,4]]))
    print(sol.minimumDistance(points = [[1,1],[1,1],[1,1]]))
    
    