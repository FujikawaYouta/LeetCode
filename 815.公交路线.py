from collections import Counter
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        '''
        以下方法构建了完整的图，每一个子图内部的节点数量最多是10^5，共有平方级别的节点
        显然会爆内存，尝试更换思路
        '''
        # # 用字典记录相邻节点
        # neighbor = dict()
        # for route in routes:
        #     for src_node in route:
        #         for dst_node in route:
        #             if src_node!=dst_node:
        #                 if src_node not in neighbor:
        #                     neighbor[src_node] = [dst_node]
        #                 else:
        #                     neighbor[src_node].append(dst_node)
        # # 用visited数组记录是否访问
        # visited = set()
        # # 用bfs，记录每一次换乘的次数
        # que = [(source,0)]
        # while que:
        #     cur_node, times = que.pop(0)
        #     for node in neighbor[cur_node]:
        #         if node == target:
        #             return times+1
        #         if node not in visited:
        #             que.append((node,times+1))
        #             visited.add(node)
        # return -1
        '''
        下面的思路是对于当前节点，找到哪些公交线路（子图）可以使用
        可以将每个节点属于第几个子图存储起来，每次只遍历子图
        '''
        station_buses = dict()
        for i,route in enumerate(routes):
            for station_id in route:
                if station_id not in station_buses:
                    station_buses[station_id] = set([i])
                else:
                    station_buses[station_id].add(i)
        que = [(source,0)]
        visited = set([source])
        visited_routes = set()
        while que:
            station_id, times = que.pop(0)
            if station_id not in station_buses:
                return -1
            for bus_id in station_buses[station_id]:
                # 对于每一个子图，遍历子节点
                if bus_id in visited_routes:
                    continue
                for node in routes[bus_id]:
                    if node == target:
                        return times+1
                    if node not in visited and node!=station_id:
                        que.append((node,times+1))
                        visited.add(node)
                visited_routes.add(bus_id)
        return -1
if __name__ == '__main__':
    sol = Solution()
    # print(sol.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12))
    print(sol.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))