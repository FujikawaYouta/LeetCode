from collections import defaultdict
class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        neighbor = defaultdict(list)
        for node1,node2,cost in edges:
            neighbor[node1].append([node2, cost])
            neighbor[node2].append([node1, cost])
        # 记录访问过的节点以计算价值
        visted_nodes={0}
        # 以0作为根节点进行图遍历
        def dfs():
            pass
            
        return 0


sol = Solution()
print(sol.maximalPathQuality(values = [0,32,10,43], 
                             edges = [[0,1,10],[1,2,15],[0,3,10]],
                             maxTime = 49))