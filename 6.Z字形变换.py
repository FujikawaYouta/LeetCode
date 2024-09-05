# 等间隔取数
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return ''.join(s[::2]+s[1::2])
        n = len(s)
        str_list = ['' for _ in range(numRows)]
        step = 1+2*(numRows-2)+1
        str_list[0]=s[::step]
        str_list[-1]=s[step//2::step]
        for i in range(1,numRows-1):
            for j in range(n//step+1):
                if i+j*step<n:
                    str_list[i]+=s[i+j*step]
                if step-i+j*step<n:
                    str_list[i]+=s[step-i+j*step]
        ans = ''
        for i in range(numRows):
            ans+=str_list[i]
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.convert(s='PAYPALISHIRING', numRows = 3))