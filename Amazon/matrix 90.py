def matrix(mat):
    n = len(mat)
    top = 0
    bottom = len(mat) - 1
    while top <= bottom:
        for i in range(n):
            temp = mat[top][i]
            mat[top][i] = mat[bottom][i]
            mat[bottom][i] = temp

        top +=1
        bottom -=1
    for i in range(n):
        for j in range(i+1,n):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i]  = temp
    return mat
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix(mat))