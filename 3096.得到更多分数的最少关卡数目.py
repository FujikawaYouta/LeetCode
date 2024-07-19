class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        n = len(possible)
        alice = [0 for _ in range(n)]
        # 先计算出完成所有关卡后总的得分，然后再递推
        total_init = sum(possible)-(n-sum(possible))
        alice[0] = 1 if possible[0]==1 else -1
        if alice[0]>total_init//2:
            return 1
        for i in range(1, n-1):
            alice[i] = alice[i-1]+(1 if possible[i]==1 else -1)
            if alice[i]>total_init//2:
                return i+1
        return -1
    
sol = Solution()
print(sol.minimumLevels(possible = [0,0,1,0]))