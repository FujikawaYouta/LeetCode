class Solution:
    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        # 最极端情况下答案为1
        ans = 1
        que = []
        # i代表bus，j代表乘客
        i,j=0,0
        # 模拟上客
        for i,bus in enumerate(buses):
            cnt = capacity
            while j<len(passengers) and passengers[j]<=bus and cnt>0:
                j+=1
                cnt-=1
        # 至此，[0,j)个乘客都可以上车        
        
        # 找插队位置
        # 如果还有空位没上满，直接返回最后一班的发车时间
        if cnt>0 and passengers[j-1]!=buses[-1]:
            return buses[-1]
        # 初始化ans为最后一个乘客的上车时间，反着找，找到第一个空位
        latest = passengers[j-1]
        while passengers[j-1]-passengers[j-2]==1 and j>1:
            j-=1
        ans = passengers[j-1]-1
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    # print(sol.latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))
    print(sol.latestTimeCatchTheBus(buses = [2], passengers = [2], capacity = 2))
    # print(sol.latestTimeCatchTheBus(buses = [5], passengers = [2,3], capacity = 10000))