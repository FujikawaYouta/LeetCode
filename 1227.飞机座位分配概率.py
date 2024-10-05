class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # 最后一个人坐到错误的位置
        return 1/n
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.nthPersonGetsNthSeat(n = 1))