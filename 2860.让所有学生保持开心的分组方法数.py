class Solution:
    def countWays(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        # 选中学生的个数取值为0,[1,n-1]和n
        for i in range(1,n-1):
            # 检查每个选取是否合法
            if nums[i-1]<i and nums[i]>i:
                ans+=1
        if 0<min(nums):
            ans+=1
        if n>max(nums):
            ans+=1
        return ans
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.countWays(nums = [6,0,3,3,6,7,2,7])) # 0 2 3 3 6 6 7 7 