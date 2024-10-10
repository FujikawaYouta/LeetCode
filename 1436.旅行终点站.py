from typing import List
from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n = len(paths)
        travel_dict = defaultdict()
        for path in paths:
            travel_dict[path[0]] = path[1]
        cur_city = paths[0][0]
        for i in range(n):
            if cur_city not in travel_dict:
                return cur_city
            cur_city = travel_dict[cur_city]
        return cur_city
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.destCity(paths = [["B","C"],["D","B"],["C","A"]]))