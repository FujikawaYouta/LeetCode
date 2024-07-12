class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        n = len(nums)
        if n%2!=0:
            return []
        alice = 0
        bob = 0
        arr = []
        for i in range(n//2):
            alice = nums[2*i]
            bob = nums[2*i+1]
            arr.append(bob)
            arr.append(alice)
        return arr

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberGame(nums = [5,4,2,3]))