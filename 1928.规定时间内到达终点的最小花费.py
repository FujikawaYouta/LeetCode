from heapq import heapify,heappush,heappop
from typing import List
from collections import defaultdict
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        neighbors = defaultdict()
        for edge in edges:
            src_node = edge[0]
            dst_node = edge[1]
            path_time = edge[2]
            if src_node not in neighbors:
                neighbors[src_node] = {(dst_node, path_time)}
            else:
                neighbors[src_node].add((dst_node, path_time))
            if dst_node not in neighbors:
                neighbors[dst_node] = {(src_node, path_time)}
            else:
                neighbors[dst_node].add((src_node, path_time))
        # 考虑bfs, 四元组(节点, 当前费用, 当前时间, 走过的节点), 会超时
        # ans = float('inf')
        # node_queue = [(0, passingFees[0], 0, {0})]
        # while len(node_queue):
        #     cur_node, cur_fee, cur_time, past_nodes = node_queue.pop(0)
        #     # 最后一个节点
        #     if cur_node == n-1:
        #         ans = min(ans, cur_fee)
        #         continue
        #     for next_node,path_time in neighbors[cur_node]:
        #         if next_node in past_nodes:
        #             continue
        #         if cur_time+path_time>maxTime:
        #             continue
        #         node_queue.append((next_node, cur_fee+passingFees[next_node],
        #                            cur_time+path_time, past_nodes|{next_node}))
        # return ans if ans!=float('inf') else -1
        # 考虑动态规划，用dp[node][time]表示在time时刻到达node时花费的最小代价
        dp = [[float('inf')]*(maxTime+1) for _ in range(n)]
        # 初始化dp
        dp[0][0] = passingFees[0]
        
        
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.minCost(maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]))