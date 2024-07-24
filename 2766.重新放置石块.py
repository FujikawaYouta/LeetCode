class Solution:
    def relocateMarbles(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        n = len(nums)
        m = len(moveFrom)
        s = set()
        for num in nums:
            s.add(num)
        for i in range(m):
            s.remove(moveFrom[i])
            s.add(moveTo[i])
        return sorted(s)
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.relocateMarbles(nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5]))
