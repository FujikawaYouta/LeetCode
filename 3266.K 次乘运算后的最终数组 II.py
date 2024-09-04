import heapq
class P:
    def __init__(self, num, idx):
        self.num = num
        self.idx = idx
    def __lt__(self, other):
        return True if self.num>other.num else False
    def p(self):
        print(self.num, self.idx)
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        n = len(nums)
        mod = int(1e9+7)
        heap = []
        for i in range(n):
            heapq.heappush(heap, P(nums[i], i))
            
        return nums
            
if __name__ == '__main__':
    sol = Solution()
    print(sol.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))