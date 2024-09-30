class Solution:
    def kthCharacter(self, k: int) -> str:
        n = k.bit_length()
        dp = [0]*(1<<n)
        ptr = 1
        for base in range(1,n+1):
            while ptr<(1<<base):
                dp[ptr]=dp[ptr-(1<<(base-1))]+1
                ptr+=1
        return chr(ord('a')+dp[k-1])
            
if __name__ == '__main__':
    sol = Solution()
    print(sol.kthCharacter(k=5))