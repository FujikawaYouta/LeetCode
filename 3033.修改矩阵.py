import copy
class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        #
        m = len(matrix)
        n = len(matrix[0])
        matrix_out = copy.deepcopy(matrix)
        for j in range(n):
            to_fill = []
            max_value = -1
            for i in range(m):
                if matrix_out[i][j]==-1:
                    to_fill.append(i)
                max_value = max(max_value, matrix_out[i][j])
            for fill_index in to_fill:
                matrix_out[fill_index][j] = max_value 
        return matrix_out

if __name__ == '__main__':
    sol = Solution()
    print(sol.modifiedMatrix(matrix=[[1,2,-1],[4,-1,6],[7,8,9]]))