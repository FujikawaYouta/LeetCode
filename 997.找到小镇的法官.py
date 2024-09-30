class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust)==0:
            if n==1:
                return 1
            return -1
        # 所有人都信任他
        # 假设第一个人信任的就是法官
        judge = [0]*(n+1)
        candidates = []
        not_judge = set()
        # 验证所有人
        for i,tru in enumerate(trust):
            judge[tru[1]]+=1
            if judge[tru[1]]==n-1:
                candidates.append(tru[1])
            not_judge.add(tru[0])
        final = []
        for candidate in candidates:
            if candidate not in not_judge:
                final.append(candidate)
        if len(final)==1:
            return final[0]
        return -1
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))
    print(sol.findJudge(n = 3, trust = [[1,3],[2,3]]))