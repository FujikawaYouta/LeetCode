from typing import List
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 倍增+二分查找
        def tripOfTime(total_time):
            trip_cnt = 0
            for t in time:
                trip_cnt+=total_time//t
            return trip_cnt
        l = 1
        r = 1
        # 倍增定界
        while tripOfTime(r)<totalTrips:
            l = r
            r *= 2
        # 二分查找结果
        while l<=r:
            m = l+(r-l)//2 # 防止溢出
            trip_cnt = tripOfTime(m)
            if trip_cnt<totalTrips:
                l = m+1
            else:
                r = m-1
        return l
    
if __name__ == '__main__':
    sol = Solution()
    # print(sol.minimumTime(time = [1,2,3], totalTrips = 5))
    print(sol.minimumTime(time = [2], totalTrips = 1))