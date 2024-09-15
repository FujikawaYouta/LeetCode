class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        n = len(b)
        b_s = [[a[i]*num for num in b] for i in range(4)]
        dp = [[-float('inf') for _ in range(n)] for _ in range(4)]
        for i in range(4):
            if i == 0:
                for j in range(n-3):
                    dp[0][j]=b_s[0][j]
            else:
                max_last = -float('inf')
                for j in range(i,n-3+i):
                    max_last = max(max_last,dp[i-1][j-1])
                    # dp[i][j]=b_s[i][j]+max(dp[i-1][i-1:j])
                    dp[i][j]=b_s[i][j]+max_last
        return max(dp[3])
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]))