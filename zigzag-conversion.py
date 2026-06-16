class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        going_down = False

        for ch in s:
            rows[curr_row] += ch

            # Change direction at top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            curr_row += 1 if going_down else -1

        return "".join(rows)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4)) 
print(sol.convert("A", 1)) 