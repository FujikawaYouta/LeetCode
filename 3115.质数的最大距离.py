class Solution:
        
    def maximumPrimeDifference(self, nums: list[int]) -> int:
        prime_table = [-1 for _ in range(max(nums)+1)]
        prime_list = [2]
        prime_table[2] = 1
        def isPrime(number):
            if number<2:
                prime_table[number]=0
                return False
            if prime_table[number]==1:
                return True
            for prime_num in prime_list:
                if number%prime_num==0:
                    prime_table[number]=0
                    return False
            prime_table[number]=1
            prime_list.append(number)
            return True
        for num, _ in enumerate(prime_table):
            isPrime(num)
        lptr = -1
        rptr = 0
        # 找最左边的素数
        for i,num in enumerate(nums):
            if isPrime(num):
                lptr = i
                break
        # 找最右边的素数
        for i,num in enumerate(nums[::-1]):
            if isPrime(num):
                rptr = -(i+1)
                break
        print('prime list=', prime_list)
        print('prime table=', prime_table)
        print('left index=', lptr)
        print('right index=', rptr)
        return len(nums)+rptr-lptr
    
sol = Solution()
nums = [4,2,9,5,3]
print(sol.maximumPrimeDifference(nums))