class Solution:
    def checkMove(self, board: list[list[str]], rMove: int, cMove: int, color: str) -> bool:
        # 从右下顺时针转到右
        step_row = [1, 1, 1, 0, -1, -1, -1, 0]
        step_col = [1, 0, -1, -1, -1, 0, 1, 1]
        # 检查每个方向是不是好线段
        n_row = len(board)
        n_col = len(board[0])
        board[rMove][cMove] = color
        central_character = board[rMove][cMove]
        for idx in range(8):
            step_idx = 0
            cur_row,cur_col = rMove,cMove
            while (cur_col>=0 and cur_col<n_col) \
                and (cur_row>=0 and cur_row<n_row) \
                and board[cur_row][cur_col]!='.':
                # 第一步必须是不同颜色
                if step_idx==1 and board[cur_row][cur_col]==central_character:
                    break
                elif step_idx>1:
                    # 结束标志
                    if board[cur_row][cur_col]==central_character:
                        return True
                step_idx+=1
                cur_row+=step_row[idx]
                cur_col+=step_col[idx]
        return False
    
sol = Solution()
# print(sol.checkMove(board = [[".",".",".","B",".",".",".","."],
#                             [".",".",".","W",".",".",".","."],
#                             [".",".",".","W",".",".",".","."],
#                             [".",".",".","W",".",".",".","."],
#                             ["W","B","B",".","W","W","W","B"],
#                             [".",".",".","B",".",".",".","."],
#                             [".",".",".","B",".",".",".","."],
#                             [".",".",".","W",".",".",".","."]],
#                             rMove = 4, cMove = 3, color = "B"))
# print(sol.checkMove(board = [[".",".",".",".",".",".",".","."],
#                             [".","B",".",".","W",".",".","."],
#                             [".",".","W",".",".",".",".","."],
#                             [".",".",".","W","B",".",".","."],
#                             [".",".",".",".",".",".",".","."],
#                             [".",".",".",".","B","W",".","."],
#                             [".",".",".",".",".",".","W","."],
#                             [".",".",".",".",".",".",".","B"]],
#                             rMove = 4, cMove = 4, color = "W"))
# print(sol.checkMove(board = [["W","W",".","B",".","B","B","."],
#                             ["W","B",".",".","W","B",".","."],
#                             ["B","B","B","B","W","W","B","."],
#                             ["W","B",".",".","B","B","B","."],
#                             ["W","W","B",".","W",".","B","B"],
#                             ["B",".","B","W",".","B",".","."],
#                             [".","B","B","W","B","B",".","."],
#                             ["B","B","W",".",".","B",".","."]],
#                             rMove = 7, cMove = 4, color = "B")) 
print(sol.checkMove(board = [["B","W",".",".",".","W",".","B"],
                            ["W","B","B","W","B","W","W","B"],
                            [".","B","W",".","W",".",".","W"],
                            [".","W","B",".","W",".",".","."],
                            ["W",".",".",".","B","W","W","."],
                            [".","B","B",".","W","W",".","W"],
                            [".",".",".","W","B","B","W","W"],
                            ["B","B","B",".",".","W","B","."]],
                            rMove = 0, cMove = 4, color = "W")) 