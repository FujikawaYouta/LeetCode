class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        occ = [0]*100
        ans = []
        for num in nums:
            if occ[num]==1:
                ans.append(num)
                if len(ans)==2:
                    return ans
            occ[num]=1
        return []