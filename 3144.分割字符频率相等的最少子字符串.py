class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            hash_s = [0]*26
            max_cnt = 0
            char_num = 0
            for j in range(i,-1,-1):
                idx = ord(s[j-1])-ord('a')
                if hash_s[idx]==0:
                    char_num+=1
                hash_s[idx]+=1
                max_cnt = max(max_cnt, hash_s[idx])
                # 合法的
                if max_cnt*char_num==i-j+1:
                    # dp[j-1]表示前面的分组数，1表示后面的1组
                    dp[i]=min(dp[i],dp[j-1]+1)
        return dp[n]
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSubstringsInPartition(s = "fabccddg"))
    print(sol.minimumSubstringsInPartition(s = "abababaccddb"))