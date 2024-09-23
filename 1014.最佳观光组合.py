class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        n = len(values)
        actual_i = [values[i]+i for i in range(n)]
        actual_j = [values[j]-j for j in range(n)]
        for i in range(1,n):
            actual_i[i] = max(actual_i[i],actual_i[i-1])
        max_sum = 0
        for j in range(1,n):
            max_sum = max(max_sum, actual_j[j]+actual_i[j-1])
        return max_sum
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScoreSightseeingPair(values = [8,1,5,2,6]))