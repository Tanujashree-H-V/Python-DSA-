class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Solution().rotate(matrix)
print(matrix)


matrix1 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
Solution().rotate(matrix1)
print(matrix1)