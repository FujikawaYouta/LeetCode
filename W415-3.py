# 错解，不一定要贪心地让每一步匹配到最长
class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        def matchString(word: str, target: str):
            m1 = len(word)
            m2 = len(target)
            m = min(m1, m2)
            for i in range(m):
                if word[i]!=target[i]:
                    return target[i:]
            return None if m1>=m2 else target[m1:]
        n = len(words)
        que = [(target,0)]
        while len(que):
            sub_target,times = que.pop(0)
            for i in range(n):
                if words[i][0]==sub_target[0]:
                    tmp = matchString(words[i], sub_target)
                    if tmp:
                        que.append((tmp,times+1))
                    else:
                        return times+1
        return -1
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.minValidStrings(words=["b","ccacc","a"], target="cccaaaacba"))