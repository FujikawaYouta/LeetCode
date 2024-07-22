class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        neighbor_table = []
        # 建立邻接表，对于每一个结点遍历他的邻居
        def calSquaredDistance(bomb1, bomb2):
            return (bomb1[0]-bomb2[0])**2+(bomb1[1]-bomb2[1])**2
        for i in range(n):
            cur_neighbor = []
            for j in range(n):
                if i==j:
                    continue
                # i-->j是可达的
                if calSquaredDistance(bombs[i], bombs[j])<=bombs[i][2]**2:
                    cur_neighbor.append(j)
            neighbor_table.append(cur_neighbor)
        # 建立好邻接表后开始遍历结点
        max_count = 1
        for i, bomb in enumerate(bombs):
            # 初始化访问结点为自己
            visited = {i}
            cur_queue = [i]
            # 广度优先搜索
            while len(cur_queue)!=0:
                cur_node = cur_queue.pop(0)
                for node in neighbor_table[cur_node]:
                    if node not in visited:
                        cur_queue.append(node)
                        visited.add(node)
            max_count = max(max_count, len(visited))
        return max_count

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumDetonation(bombs = [[2,1,3],[6,1,4]]))
    print(sol.maximumDetonation(bombs = [[1,1,5],[10,10,5]]))
    print(sol.maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))

