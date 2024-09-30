class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        # n = len(operations)
        # dp = [0]*(1<<n)
        # ptr = 1
        # for i in range(n):
        #     while ptr<(1<<i+1):
        #         if operations[i]==0:
        #             dp[ptr]=dp[ptr-(1<<(i))]
        #         else:
        #             dp[ptr]=dp[ptr-(1<<(i))]+1
        #         ptr+=1
        # return chr(ord('a')+dp[k-1])
        # 我只需要第k个，其他的能不能不要遍历？
        # 记录距离
        diff = 0
        k = k-1
        while k>0:
            m = (k).bit_length()-1
            k = k&(~(1<<m))
            diff+=1 if operations[m]==1 else 0
        return chr(ord('a')+diff%26)
        
            
if __name__ == '__main__':
    sol = Solution()
    # print(sol.kthCharacter(k=4, operations=[1,0]))
    # print(sol.kthCharacter(k=5, operations=[0,0,0]))
    # print(sol.kthCharacter(k=10, operations=[0,1,0,1]))
    print(sol.kthCharacter(k=100000000000000, operations=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
    # print(sol.kthCharacter(k=30537342, operations=[0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0]))