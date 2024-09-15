class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0]*(n+1)
        l_ptr = 0
        ans = 0
        for r_ptr in range(n):
            if prizePositions[r_ptr]-prizePositions[l_ptr]<=k:
                dp[r_ptr+1]=r_ptr-l_ptr+1
            while prizePositions[r_ptr]-prizePositions[l_ptr]>k:
                l_ptr+=1
            dp[r_ptr+1] = max(dp[r_ptr+1], dp[r_ptr])
            ans = max(ans, (r_ptr-l_ptr+1)+dp[l_ptr])
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximizeWin(prizePositions = [1,1,2,2,3,3,5,8], k = 2))