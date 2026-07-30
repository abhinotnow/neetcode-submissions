class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row = i//3
                col = j//3
                index = row*3 + col
                if board[i][j] in boxes[index]:
                    return False
                else:
                    boxes[index].add(board[i][j])
                #row col check
                if any(board[i][j] in x for x in (rows[i], cols[j])):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
        return True
                

