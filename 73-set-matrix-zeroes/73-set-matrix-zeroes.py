class Solution(object):
    def setZeroes(self, matrix):
        row=[1 for i in range(len(matrix))]
        column=[1 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=0
                    column[j]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i]==0 or column[j]==0:
                    matrix[i][j]=0
        