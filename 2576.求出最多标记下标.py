class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums.sort()
        doubled_nums = [num*2 for num in nums]
        if nums[-1]<doubled_nums[0]:
            return 0
        fast_ptr = 0
        slow_ptr = 0
        n = len(nums)
        ans = 0
        while fast_ptr<n:
            while fast_ptr<n and nums[fast_ptr]<doubled_nums[slow_ptr]:
                fast_ptr+=1
            if fast_ptr>=n:
                break
            ans+=2
            print(nums[fast_ptr], doubled_nums[slow_ptr])
            fast_ptr+=1
            slow_ptr+=1
        return min(n,ans)
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxNumOfMarkedIndices(nums = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]))