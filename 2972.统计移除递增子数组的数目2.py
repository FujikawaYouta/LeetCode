class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        # 设计双指针来遍历整个数组
        n = len(nums)
        l_ptr = 0
        r_ptr = n
        
        ans = 0
        nums+=[float('inf')]
        # 找到左指针的最远位置
        for _ in range(n-1):
            if nums[l_ptr]<nums[l_ptr+1]:
                l_ptr+=1
        if l_ptr == n-1:
            return n*(n+1)//2
        # 对于每一个右指针，加入左指针的子集
        while r_ptr>=n-1 or nums[r_ptr]<nums[r_ptr+1]:
            while l_ptr!=-1 and nums[r_ptr]<=nums[l_ptr]:
                l_ptr-=1
            if r_ptr==n or l_ptr==-1 or nums[r_ptr]>nums[l_ptr]:
                ans+=l_ptr+2 # 例如 l_ptr=0 对应两个结果，即[{nums[0]}, 空集]
                r_ptr-=1
                continue
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.incremovableSubarrayCount(nums = [1,2,3,4]))
    print(sol.incremovableSubarrayCount(nums = [6,5,7,8]))
    print(sol.incremovableSubarrayCount(nums = [8,7,6,6]))
    print(sol.incremovableSubarrayCount(nums = [8,1,2]))
