class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        # 设计双重循环来遍历每一个子数组
        def isSorted(cur_nums):
            n_cur = len(cur_nums)
            if n_cur==1:
                return True
            for i in range(1, n_cur):
                if cur_nums[i]<=cur_nums[i-1]:
                    return False
            return True
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                # 移除[i,j]后的数组
                if isSorted(nums[:i]+nums[j:]):
                    ans+=1
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.incremovableSubarrayCount(nums = [1,2,3,4]))
    print(sol.incremovableSubarrayCount(nums = [6,5,7,8]))
    print(sol.incremovableSubarrayCount(nums = [8,7,6,6]))
