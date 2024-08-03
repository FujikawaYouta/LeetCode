class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for _ in range(n+5)]
        idx = 2
        # 找出素数
        while idx<n+5:
            if isPrime[idx] == True:
                for i in range(2, (n+5)//idx+1):
                    if i*idx>=n+5:
                        continue
                    isPrime[i*idx]=False
            idx+=1
        # 求素数前缀和
        pre_sum = [0,0]
        for i in range(2, n+1):
            if isPrime[i]==True:
                pre_sum.append(pre_sum[-1]+1)
            else:
                pre_sum.append(pre_sum[-1])
        return pre_sum[n-1]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(n = 10000))