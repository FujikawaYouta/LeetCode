class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        n = len(edges)
        scores = [0]*n
        max_score = [0,n]
        for i,edge in enumerate(edges):
            scores[edge] += i
            if scores[edge]>max_score[0]:
                max_score[0]=scores[edge]
                max_score[1]=edge
            elif scores[edge]==max_score[0] and edge<max_score[1]:
                max_score[1]=edge
        return max_score[1]
if __name__ == '__main__':
    sol = Solution()
    print(sol.edgeScore(edges = [1,0,0,0,0,7,7,5]))