class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        def diffOfPosition(digits_hash: list):
            pre_sum = [0 for _ in range(10)]
            pre_sum[0] = digits_hash[0]
            for i in range(1,10):
                pre_sum[i]=pre_sum[i-1]+digits_hash[i]
            ans = 0
            for i in range(9,0,-1):
                ans += digits_hash[i]*pre_sum[i-1]
            return ans
        n = len(nums)
        ans = 0
        tmp = nums[0]
        while tmp>0:
            digits_hash = [0 for _ in range(10)]
            for i in range(n):
                digits_hash[nums[i]%10]+=1
                nums[i]//=10
            ans += diffOfPosition(digits_hash)
            tmp//=10
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumDigitDifferences(nums = [50,28,48]))