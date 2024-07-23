def degree(matrix):
    n = len(matrix)
    top = 0
    bottom = len(matrix) - 1
    while top<=bottom:
        for i in range(n):
            temp = matrix[top][i]
            matrix[top][i] = matrix[bottom][i]
            matrix[bottom][i] = temp
        top+=1
        bottom-=1
    for i in range(n):
        for j in range(i+1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(degree(matrix))