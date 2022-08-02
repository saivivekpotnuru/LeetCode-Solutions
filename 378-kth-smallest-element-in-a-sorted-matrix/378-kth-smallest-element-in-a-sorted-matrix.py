class Solution(object):
    def kthSmallest(self, matrix, k):
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l.append(matrix[i][j])
        l.sort()
        return l[k-1]
        