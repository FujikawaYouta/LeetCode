class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0 for _ in range(32)]
        dp[0]=1
        dp[1]=1
        for i in range(2,32):
            dp[i]=dp[i-1]+dp[i-2]
        one_appear = 0
        ans = 0
        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                ans += dp[i + 1]
                if one_appear == 1:
                    break
                one_appear = 1
            else:
                one_appear = 0
            if i == 0:
                ans += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.findIntegers(n = 25))
    print(sol.findIntegers(n = 100000000))