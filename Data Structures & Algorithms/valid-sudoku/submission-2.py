

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen = set()
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

        
        for j in range(9):
            seen = set()
            for i in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        value = board[i][j]
                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)

        return True