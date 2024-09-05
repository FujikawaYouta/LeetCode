# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_ptr = 0
        r_ptr = 0
        max_len = 0
        n = len(s)
        visited_char = set()
        while r_ptr<n:
            if s[r_ptr] not in visited_char:
                visited_char.add(s[r_ptr])
            else:
                while s[l_ptr]!=s[r_ptr]:
                    visited_char.remove(s[l_ptr])
                    l_ptr+=1
                l_ptr+=1
            max_len = max(max_len, r_ptr-l_ptr+1)
            r_ptr+=1
        return max_len
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s = "abcabcbb"))