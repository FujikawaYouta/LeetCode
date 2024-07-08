class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        pre_sum = [0 for _ in range(n+1)]
        suf_sum = [0 for _ in range(n+1)]
        # 前缀和
        for idx, num in enumerate(nums):
            pre_sum[idx+1] = pre_sum[idx] + num
        # 后缀和
        for idx, num in enumerate(nums[::-1]):
            suf_sum[idx+1] = suf_sum[idx] + num
        # 找最左配对
        for idx in range(n):
            if pre_sum[idx]==suf_sum[n-idx-1]:
                return idx
        return -1
    
sol = Solution()
print(sol.pivotIndex(nums = [1, 7, 3, 6, 5, 6]))
print(sol.pivotIndex(nums = [1, 7, 3, 0, 0, 5, 6]))
print(sol.pivotIndex(nums = [1, 2, 3]))
print(sol.pivotIndex(nums = [2, 1, -1]))