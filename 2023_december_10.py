class Solution(object):
    def transpose(self, matrix):
        longueur=len(matrix)
        longueurTab=len(matrix[0])
        result=[[0]*longueur for _ in range(longueurTab)]
        for i in range(longueurTab):
            for j in range(longueur):
                result[i][j]=matrix[j][i]
        return result