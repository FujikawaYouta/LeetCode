from collections import defaultdict
class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        neighbour = defaultdict(list)
        for node1,node2,cost in edges:
            neighbour[node1].append([node2, cost])
            neighbour[node2].append([node1, cost])
        # 记录访问过的节点以计算价值
        visted_nodes={0}
        max_value=values[0]
        # 以0作为根节点进行图遍历
        def dfs(root_node, visited, current_time):
            for node,cost in neighbour[root_node]:
                # 要终止遍历，且当前是起点节点
                if root_node==0:
                    cur_value = 0
                    for i in visited:
                        cur_value+=values[i]
                    nonlocal max_value
                    max_value=max(max_value, cur_value)
                # 还可以继续遍历
                if current_time+cost<=maxTime:
                    next_visited = visited.copy()
                    next_visited.add(node)
                    dfs(node, next_visited, current_time+cost)
        dfs(0, visted_nodes, 0)
        return max_value


sol = Solution()
print(sol.maximalPathQuality(values = [0,32,10,43], 
                             edges = [[0,1,10],[1,2,15],[0,3,10]],
                             maxTime = 49))
# print(sol.maximalPathQuality(values = [5,10,15,20],
#                              edges = [[0,1,10],[1,2,10],[0,3,10]],
#                              maxTime = 30))