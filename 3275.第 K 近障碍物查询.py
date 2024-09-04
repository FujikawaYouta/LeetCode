from heapq import heappush, heappop
class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        def distance(point):
            return int(abs(point[0])+abs(point[1]))
        n = len(queries)
        ans = [-1 for _ in range(n)]
        h = []
        for i in range(n):
            dis = distance(queries[i])
            # 默认最小堆，负号变为最大堆
            heappush(h, -dis)
            if i>k-1:
                tmp = -heappop(h)
                ans[i]=-h[0]
            if i==k-1:
                ans[i]=-h[0]
        return ans
        
if __name__ == '__main__':
    sol = Solution()
    # print(sol.resultsArray(queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2))
    # print(sol.resultsArray(queries = [[5,5],[4,4],[3,3]], k = 1))
    print(sol.resultsArray(queries = [[6,10],[0,-10],[2,-6]], k = 2))