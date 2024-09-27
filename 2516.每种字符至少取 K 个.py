class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0]*3
        for ch in s:
            cnt[ord(ch)-ord('a')]+=1
        if cnt[0]<k or cnt[1]<k or cnt[2]<k:
            return -1
        slow_ptr = 0
        ans = 0
        for fast_ptr,ch in enumerate(s):
            cur_idx = ord(ch)-ord('a')
            cnt[cur_idx]-=1
            if cnt[cur_idx]<k:
                while ord(s[slow_ptr])-ord('a')!=cur_idx:
                    cnt[ord(s[slow_ptr])-ord('a')]+=1
                    slow_ptr+=1
                cnt[ord(s[slow_ptr])-ord('a')]+=1
                slow_ptr+=1
            ans = max(ans, fast_ptr-slow_ptr+1)
        return len(s)-ans
        
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.takeCharacters(s = "aabaaaacaabc", k = 2))