class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # 其实只需要判断所有长度为limit+1的子数组是不是包含0和1
        # 考虑构造dp[i][j][k]表示之前出现过i个0，j个1，以k(0或1)结尾的可行方案
        # 对于dp[i][j][0]:
        # j = 0 且 i <= min(limit, zero)时，符合条件的只有一种方案
        # j = 0 且 i > min(limit, zero)时，没有符合条件的方案
        # i = 0 时，与0结尾冲突，没有符合条件的方案
        # i > 0 且 j > 0时dp[i][j][0]与之前表项的关系为：
        # 对于dp[i-1][j][1]来说，可以完全继承(+=)
        # 对于dp[i-1][j][0]来说，如果i<limit+1 \
        # (也就是加入一个0以后肯定不会破坏“所有长度为limit+1的子数组是不是包含0和1”这一条件)
        # 这部分可以完全继承
        # 而如果i>=limit+1，有且只有一种方案不可行，即在末尾出现了连续limit个0，
        # 再加一个0会导致不符合条件，所以减掉这种情况就可以解决
        # 同理可以设计出dp[i][j][1]的递推关系
        mod = int(1e9+7)
        dp = [[[0, 0] for _ in range(one+1)] for __ in range(zero+1)]
        # 初始化dp
        for i in range(zero+1):
            if i<=min(limit, zero):
                dp[i][0][0] = 1
        for j in range(one+1):
            if j<=min(limit, one):
                dp[0][j][1] = 1
        for i in range(1,zero+1):
            for j in range(1,one+1):
                # 对于dp[i][j][0]
                if i>limit:
                    dp[i][j][0] = (dp[i-1][j][1]+dp[i-1][j][0]-dp[i-1-limit][j][1])%mod
                else:
                    dp[i][j][0] = (dp[i-1][j][1]+dp[i-1][j][0])%mod
                # 对于dp[i][j][1]
                if j>limit:
                    dp[i][j][1] = (dp[i][j-1][0]+dp[i][j-1][1]-dp[i][j-1-limit][0])%mod
                else:
                    dp[i][j][1] = (dp[i][j-1][0]+dp[i][j-1][1])%mod
        return (dp[zero][one][0]+dp[zero][one][1])%mod
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfStableArrays(zero = 1, one = 1, limit = 2))
    print(sol.numberOfStableArrays(zero = 1, one = 2, limit = 1))
    print(sol.numberOfStableArrays(zero = 3, one = 3, limit = 2))