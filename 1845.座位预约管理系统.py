from heapq import heappop,heappush,heapify
class SeatManager:

    def __init__(self, n: int):
        self.n = n+1
        # self.seats = [False]*(n+1)
        self.first_seat = [i for i in range(1,1+n)]
        heapify(self.first_seat)
        pass

    def reserve(self) -> int:
        ans = heappop(self.first_seat)
        # self.seats[ans] = True
        # 更新first_seat
        # 需要维护一个最小值
        return ans

    def unreserve(self, seatNumber: int) -> None:
        # self.seats[seatNumber] = False
        heappush(self.first_seat, seatNumber)
        pass


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
if __name__ == '__main__':
    obj = SeatManager(n=2)
    param_1 = obj.reserve()
    param_2 = obj.unreserve(1)
    param_3 = obj.reserve()
    param_4 = obj.reserve()
    param_5 = obj.unreserve(2)
    param_6 = obj.reserve()
    param_7 = obj.unreserve(1)
    param_8 = obj.reserve()
    param_9 = obj.unreserve(2)
    param_10 = obj.reserve()
    print('done.')