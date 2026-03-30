rows=int(input("enter the number of rows: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(rows):
        el=int(input("enter the element: "))
        row.append(el)
    matrix.append(row)
print("the matrix is:", matrix)
print(sum(matrix[0]),sum(matrix[1]),sum(matrix[2]))
