class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        candidates = []
        for word in wordDict:
            n_cur = len(word)
            if word == s[:n_cur]:
                if n_cur==n:
                    return True
                candidates.append([word, n_cur])
                
        cur_idx = 0
        while len(candidates)>0:
            start_idx = candidates[cur_idx][1]
            for word in wordDict:
                end_idx = start_idx+len(word)
                if word == s[start_idx:end_idx]:
                    if end_idx==n:
                        return True
                    candidates.append([word, end_idx])
            candidates.pop(0)
        return False

    
if __name__=='__main__':
    sol = Solution()
    print(sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
    print(sol.wordBreak(s = "a", wordDict = ["a"]))