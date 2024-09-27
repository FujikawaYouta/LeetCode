class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        def sumOfDigit(num):
            res = 0
            while num>10:
                res+=num%10
                num//=10
            return res
        sum_num = sum(nums)
        sum_digit = 0
        for num in nums:
            sum_digit+=sumOfDigit(num)
        return sum_num-sum_digit
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.differenceOfSum(nums = [1,15,6,3]))