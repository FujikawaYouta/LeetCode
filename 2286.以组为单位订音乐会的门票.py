class BookMyShow:
    def __init__(self, n: int, m: int):
        # 每一排一个指针
        self.ptrs = [0]*n
        # 用来维护区间最小值
        self.area_min = [0]*n
        # 用来维护区间的和
        self.area_sum = [0]*n
        
        self.rows = n
        self.cols = m

    def gather(self, k: int, maxRow: int) -> list[int]:
        m = self.rows
        n = self.cols
        for cur_row in range(maxRow+1):
            if k<=n-self.ptrs[cur_row]:
                ans = [cur_row, self.ptrs[cur_row]]
                self.ptrs[cur_row]+=k
                return ans
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        m = self.rows
        n = self.cols
        cus_sum = sum(self.ptrs)
        if k>cus_sum:
            return False
        for cur_row in range(maxRow+1):
            if k>n-self.ptrs[cur_row]:
                k-=n-self.ptrs[cur_row]
                self.ptrs[cur_row]=n
            else:
                self.ptrs[cur_row]+=k
                break
        return True


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)

if __name__ == '__main__':
    obj = BookMyShow(2,5)
    param_1 = obj.gather(4,0)
    param_2 = obj.gather(2,0)
    param_3 = obj.scatter(5,1)
    param_4 = obj.scatter(5,1)
    # obj = BookMyShow(5,9)
    # param_1 = obj.gather(10,1)
    # param_2 = obj.scatter(3,3)
    # param_3 = obj.gather(9,1)
    # param_4 = obj.gather(10,2)
    # param_5 = obj.gather(2,0)
    print('done.')