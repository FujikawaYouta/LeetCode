class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        ans = tickets[k]
        n = len(tickets)
        for i in range(k):
            ans += min(tickets[i],tickets[k])
        for i in range(k+1,n):
            ans += min(tickets[i],tickets[k]-1)
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.timeRequiredToBuy(tickets = [2,3,2], k = 2))