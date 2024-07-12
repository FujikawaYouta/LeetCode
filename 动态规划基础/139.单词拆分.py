class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        m = len(s)
        reachable_idx = [0]
        wordDict = set(wordDict)
        for cur_idx in range(1, m+1):
            for start_idx in reachable_idx:
                if s[start_idx:cur_idx] in wordDict:
                    reachable_idx.append(cur_idx)
                    break
        return m==reachable_idx[-1]
    
if __name__=='__main__':
    sol = Solution()
    print(sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
    print(sol.wordBreak(s = "a", wordDict = ["a"]))
    print(sol.wordBreak(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))