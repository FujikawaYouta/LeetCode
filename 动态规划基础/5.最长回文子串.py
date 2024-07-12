class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 奇数回文串
        max_len = 1
        max_sub = s[0]
        for i in range(n):
            length = 1
            while i-length>=0 and i+length<n and s[i-length]==s[i+length]:
                length+=1
            if 2*length-1>max_len:
                max_len = 2*length-1
                max_sub = s[i-length+1:i+length]
        # 偶数回文串
        for i in range(1,n):
            if s[i]==s[i-1]:
                length = 1
                while i-1-length>=0 and i+length<n and s[i-1-length]==s[i+length]:
                    length+=1
                if 2*length>max_len:
                    max_len = 2*length
                    max_sub = s[i-length:i+length]
        return max_sub
    
if __name__=='__main__':
    sol = Solution()
    print(sol.longestPalindrome(s = "babad"))
    print(sol.longestPalindrome(s = "cbbd"))