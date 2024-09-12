class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        fs = {}
        records = [[0]*3 for _ in range(k+1)]
        for x in nums:
            if x not in fs:
                fs[x]=[0]*3
            f = fs[x]
            # 因为需要用到j-1的值，为了防止覆盖的数影响，倒序遍历
            for j in range(k,-1,-1):
                # 相等的情况
                f[j]+=1
                # 不等的情况，保证j-1可以访问
                if j>0:
                    mx1,mx2,num = records[j-1]
                    f[j]=max(f[j], (mx1 if num!=x else mx2)+1)
                # 更新j情况下的records
                if records[j][0]<f[j]:
                    if records[j][2]!=x:
                        records[j][2]=x
                        records[j][1]=records[j][0]
                    records[j][0]=f[j]
                elif records[j][1]<f[j] and records[j][2]!=x:
                    records[j][1]=f[j]
        return records[k][0]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumLength(nums = [1,2,1,1,3], k = 2))