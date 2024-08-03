class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        # 先计算前缀和
        n = len(arr)
        # dp[i]表示以第i个元素（可能被删除）为结尾的子数组
        # 第一个元素表示不删除元素的最大结果
        # 第二个元素表示删除某一个元素的最大结果
        dp = [[0,0] for _ in range(n)]
        dp[0][0]=arr[0]
        dp[0][1]=0
        ans = arr[0]
        for i in range(1, n):
            # 一个也不删除，但是因为有自己，所以之前的可以不取
            dp[i][0] = max(dp[i-1][0],0)+arr[i]
            ans = max(ans, dp[i][0])
            # 删除之前的或者删除自己
            dp[i][1] = max(dp[i-1][1]+arr[i], dp[i-1][0])
            ans = max(ans, dp[i][1]) if i>1 else ans
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSum(arr = [1,-2,0,3]))
    print(sol.maximumSum(arr = [2,1,-2,-5,-2]))
    print(sol.maximumSum(arr = [-7,6,1,2,1,4,-1]))