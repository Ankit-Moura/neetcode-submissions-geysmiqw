class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen_row = [set() for _ in range(9)]
        seen_col = [set() for _ in range(9)]
        seen_box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_row[i]:
                    return False
                else:
                    seen_row[i].add(board[i][j])
                
                if board[i][j] in seen_col[j]:
                    return False
                else:
                    seen_col[j].add(board[i][j])
                
                box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in seen_box[box_index]:
                    return False
                else:
                    seen_box[box_index].add(board[i][j])

        return True