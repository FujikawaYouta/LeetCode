class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        # 尽可能让左边具有更多的a
        # a-z共26个字母距离最近是a(0)，最远是n(13)
        # 到a的距离是min('x'-'a', 26-('x'-'a'))
        def characterDistance(c: str) -> int:
            return min(ord(c)-ord('a'), 26-(ord(c)-ord('a')))
        n = len(s)
        s_list = list(s)
        for i in range(n):
            cur_distance = characterDistance(s[i])
            # 可以替换为a
            if k>=cur_distance:
                k-=cur_distance
                s_list[i]='a'
            else:
                s_list[i] = chr(ord(s[i])-k)
                k = 0
        return ''.join(s_list)
if __name__ == '__main__':
    sol = Solution()
    print(sol.getSmallestString(s = "zbbz", k = 3))