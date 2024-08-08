class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        min_num1 = float('inf')
        min_num2 = float('inf')
        for num in nums1:
            min_num1 = min(min_num1, num)
        for num in nums2:
            min_num2 = min(min_num2, num)
        return min_num2-min_num1
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.addedInteger(nums1 = [2,6,4], nums2 = [9,7,5]))