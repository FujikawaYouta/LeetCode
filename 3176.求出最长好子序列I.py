class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
    #     n = len(nums)
    #     if n==0:
    #         return 0
    #     dp = [[0 for _ in range(k+1)] for _ in range(n)]
    #     # dp[i][j]表示nums[:i]在j次不同的情况下的 最大子序列长度
    #     for i in range(n):
    #         dp[i][0]=1
    #     # dp[1][1]=dp[0][0]+1 if nums[1]!=nums[0]
    #     # dp[1][0]=dp[0][0]+1 if nums[1]==nums[0]
    #     max_val = 1
    #     for i in range(1,n):
    #         # 相等的情况
    #         for j in range(0,min(i,k)+1):
    #             for t in range(i):
    #                 if nums[t]==nums[i]:
    #                     dp[i][j]=max(dp[i][j],dp[t][j]+1)
    #                     max_val=max(max_val, dp[i][j])
    #         # 不等的情况
    #         for j in range(1,min(i,k)+1):
    #             for t in range(i):
    #                 if nums[t]!=nums[i]:
    #                     dp[i][j]=max(dp[i][j],dp[t][j-1]+1)
    #                     max_val=max(max_val, dp[i][j])
    #     return max_val
    
    # 题解：
        # fs = {}
        # records = [[0] * 3 for _ in range(k + 1)]
        # for x in nums:
        #     if x not in fs:
        #         fs[x] = [0] * (k + 1)
        #     f = fs[x]
        #     for j in range(k, -1, -1):
        #         # 表示相同的情况
        #         f[j] += 1
        #         if j > 0:
        #             # 表示不同的情况
        #             mx, mx2, num = records[j - 1]
        #             f[j] = max(f[j], (mx if x != num else mx2) + 1)

        #         # records[j] 维护 fs[.][j] 的 mx, mx2, num
        #         # 当前能选的最大长度
        #         v = f[j]
        #         p = records[j]
        #         # 当前能选的最大长度超过记录
        #         if v > p[0]:
        #             # 如果当前数字和维护的数字不一样
        #             if x != p[2]:
        #                 p[2] = x
        #                 p[1] = p[0]
        #             p[0] = v
        #         elif x != p[2] and v > p[1]:
        #             p[1] = v
        # return records[k][0]
        fs = {}
        records = [[0]*3 for _ in range(k+1)]
        for x in nums:
            # 读取到记录
            if x not in fs:
                fs[x]=[0]*(k+1)
            f = fs[x]
            for j in range(k,-1,-1):
                # 相同的情况
                f[j]+=1
                # 不同的情况
                if j>0:
                    mx,mx2,num=records[j-1]
                    f[j]=max(f[j],(mx if num!=x else mx2)+1)
                # 更新records
                if f[j]>records[j][0]:
                    if records[j][2]!=x:
                        records[j][1]=records[j][0]
                        records[j][2]=x
                    records[j][0]=f[j]
                elif x!=records[j][2] and f[j]>records[j][1]:
                    records[j][1]=f[j]
        return records[k][0]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumLength(nums = [1,2,1,1,3], k = 2))