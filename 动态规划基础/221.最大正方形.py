class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # 记录每个点作为右下角点的最大正方形
        dp = [[int(row_col) for row_col in row] for row in matrix]
        max_len = 0
        # 第一行不用搜索
        for i in range(m):
            for j in range(n):
                if int(matrix[i][j])==1:
                    if max_len==0:
                        max_len=1
                    if i*j==0:
                        continue
                # 对于每一个边长尝试遍历
                    k = min(dp[i-1][j], dp[i][j-1])
                    for cur_k in range(k+2)[::-1]:
                        if cur_k<2:
                            continue
                        if  int(matrix[i-cur_k+1][j-cur_k+1])==1:
                            dp[i][j]=cur_k
                            max_len=max(cur_k, max_len)
                            break
        return max_len**2

if __name__=='__main__':
    sol = Solution()
    print(sol.maximalSquare(matrix = [["1","1","1","1","0"],
                                      ["1","1","1","1","0"],
                                      ["1","1","1","1","1"],
                                      ["1","1","1","1","1"],
                                      ["0","0","1","1","1"]]))