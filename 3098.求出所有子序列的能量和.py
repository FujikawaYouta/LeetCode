from collections import defaultdict
class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mod = int(1e9+7)
        inf = float('inf')
        dp = [[defaultdict(int) for _ in range(k+1)] for __ in range(n)]
        nums.sort()
        res = 0
        # i作为最后一个元素
        for i in range(n):
            dp[i][1][inf] = 1
            # j作为第一个元素
            for j in range(i):
                diff = nums[i]-nums[j]
                # 能量为p的子序列
                for p in range(2, k+1):
                    for v,cnt in dp[j][p-1].items():
                        dp[i][p][min(diff,v)] = (dp[i][p][min(diff, v)] + cnt) % mod
            for v, cnt in dp[i][k].items():
                res = (res + v * cnt % mod) % mod
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumOfPowers(nums = [1,2,3,4], k = 3))