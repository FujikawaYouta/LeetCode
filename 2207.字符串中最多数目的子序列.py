# 三次遍历，有一次遍历的更优解
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = len(text)
        suf = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suf[i]=suf[i+1]
            if text[i]==pattern[1]:
                suf[i]+=1
        pre = [0]*(n+1)
        for i in range(1,n+1):
            pre[i]=pre[i-1]
            if text[i-1]==pattern[0]:
                pre[i]+=1
        # 原来有多少个
        ans = 0
        for i,ch in enumerate(text):
            if ch==pattern[0]:
                ans+=suf[i+1]
        # 插入pattern[0]，插最前面
        ans0 = ans+suf[0]
        # 插入pattern[1]，插最后面
        ans1 = ans+pre[-1]
        return max(ans0, ans1)
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSubsequenceCount(text = "fwymvreuftzgrcrxczjacqovduqaiig", pattern = "yy"))