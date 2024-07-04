class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # 获取各个数位的值，并求和
        origin_x = x
        sum = 0
        while x!=0:
            sum+=x%10
            x//=10
        # 用求和结果求余数，为零返回求和结果，否则返回-1
        return sum if origin_x%sum==0 else -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumOfTheDigitsOfHarshadNumber(23))