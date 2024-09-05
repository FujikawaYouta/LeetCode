class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)

if __name__ == '__main__':
    sol = Solution()
    print(sol.clearDigits('ca34'))