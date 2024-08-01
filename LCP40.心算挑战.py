class Solution:
    def maxmiumScore(self, cards: list[int], cnt: int) -> int:
        ans = 0
        n = len(cards)
        cards = sorted(cards)[::-1]
        pre = [0 for _ in range(cnt)]
        min_odd = float('inf')
        min_even = float('inf')
        for i in range(cnt):
            if i>0:
                pre[i] = pre[i-1]+cards[i]
            else:
                pre[0] = cards[0]
            if cards[i]%2==1:
                min_odd = cards[i]
            else:
                min_even = cards[i]
        if pre[cnt-1]%2==0:
            return pre[cnt-1]
        # 如果不是偶数，要么用一个ans外的最大偶数替换ans中的最小奇数，
        # 要么用一个ans外的最大奇数替换ans中的最小偶数
        for i in range(cnt, n):
            if cards[i]%2==0:
                ans=pre[cnt-1]+cards[i]-min_odd
                break
        for i in range(cnt, n):
            if cards[i]%2==1:
                ans=max(ans, pre[cnt-1]+cards[i]-min_even)
                break
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxmiumScore(cards=[9,5,9,1,6,10,3,4,5,1], cnt=2))
    print(sol.maxmiumScore(cards=[1,2,8,9], cnt=3))