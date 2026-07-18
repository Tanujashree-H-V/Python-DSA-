class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                num = board[i][j]

                # Calculate box index
                box = (i // 3) * 3 + (j // 3)

                if num in rows[i]:
                    return False

                if num in cols[j]:
                    return False

                if num in boxes[box]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

        return True
    
    
board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

print(Solution().isValidSudoku(board))