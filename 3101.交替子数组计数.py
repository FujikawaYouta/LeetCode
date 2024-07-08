class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        # 如果一个长为n的数组是交替子数组，
        # 那么他的所有子数组都是交替子数组，
        # 对应个数为n*(n+1)/2
        last_sub = -1
        cur_sub = 0
        offset = 0
        n = len(nums)
        ans = 0
        for idx in range(1,n):
            if nums[idx]!=nums[idx-1]:
                cur_sub=idx
            else:
                if last_sub==cur_sub:
                    ans+=1
                    offset+=1
                else:
                    n_sub = cur_sub-last_sub-offset
                    offset=0
                    ans+=n_sub*(n_sub+1)//2
                    last_sub = cur_sub
        if cur_sub==n-1:
            n_sub = cur_sub-last_sub-offset
            ans+=n_sub*(n_sub+1)//2
        elif last_sub==cur_sub:
            ans+=1
        return ans
    
sol = Solution()
print(sol.countAlternatingSubarrays(nums = [0,1,1,1]))# 5
print(sol.countAlternatingSubarrays(nums = [1,0,1,0]))# 10
print(sol.countAlternatingSubarrays(nums = [1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1])) # 55+21=76
print(sol.countAlternatingSubarrays(nums = [1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1])) # 56+21=77
print(sol.countAlternatingSubarrays(nums = [0,1,0,1,0,1,0,0,0,1])) # 28+1+3=32