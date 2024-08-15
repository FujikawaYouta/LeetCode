class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        # dp[j]表示以j结尾数组能最远覆盖的特殊子数组的长度，最少为1
        dp = [1 for _ in range(n)]
        for i in range(1,n):
            if nums[i]%2!=nums[i-1]%2:
                dp[i]=dp[i-1]+1
        return [query[1]-query[0]+1<=dp[query[1]] for query in queries]

if __name__ == '__main__':
    sol = Solution()
    print(sol.isArraySpecial(nums=[1,1], queries=[[0,1]]))
    print(sol.isArraySpecial(nums=[2,2], queries=[[0,0]]))
    print(sol.isArraySpecial(nums=[3,6,2,1], queries=[[0,1]]))