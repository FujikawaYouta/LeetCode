from heapq import heappush,heappop
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 从0开始
        k -= 1
        dis = [float('inf')]*n
        dis[k] = 0
        ans = 0
        # 表示src->dst的最短距离
        g = [[float('inf')]*n for _ in range(n)]
        for src,dst,cost in times:
            g[src-1][dst-1] = cost
        # reachable = [False]*n
        # while True:
        #     cur_node = -1
        #     # 确定当前节点是距离最小的节点
        #     for i in range(n):
        #         if not reachable[i] and (cur_node==-1 or dis[cur_node]>dis[i]):
        #             cur_node = i
        #     # 图不连通
        #     if dis[cur_node]==float('inf'):
        #         return -1
        #     # 所有节点都已经遍历过了
        #     if cur_node == -1:
        #         return ans
        #     # 求出dis的最大值
        #     ans = dis[cur_node]
        #     # 当前节点是可达的
        #     reachable[cur_node]=True
        #     # 更新所有邻节点
        #     for i,cost in enumerate(g[cur_node]):
        #         dis[i] = min(dis[i], dis[cur_node]+cost)
        # 寻找最小值的这个动态过程可以通过堆来优化
        min_heap = [(0,k)]
        while len(min_heap):
            cur_cost,cur_node = heappop(min_heap)
            if cur_cost>dis[cur_node]:
                continue
            for i,cost in enumerate(g[cur_node]):
                if cur_cost+cost<dis[i]:
                    dis[i] = cur_cost+cost
                    heappush(min_heap, (cur_cost+cost, i))
        return max(dis)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))