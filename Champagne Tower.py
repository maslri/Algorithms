# https://leetcode.com/problems/champagne-tower/description/?envType=daily-question&envId=2023-09-24

class Solution:

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float :
        matrix = []
        row  = 0
        index_row = 0
        while poured :
            if matrix[row][index_row] == 1 :
                matrix[row + 1][index_row] += 0.5
                matrix[row + 1][index_row + 1] += 0.5
            else :
                matrix[row][index_row] + 1
            poured -= 1
        else :
            return matrix[query_row][query_glass]
    
    def doPoured(matrix : list, row : int, index_row : int) -> list :
        if matrix[row][index_row] == 1 :
            pass
        else :
            







poured1 , query_row1 , query_glass1 = 1
poured2 , query_row2 , query_glass2 = 2 , 1 , 1
poured3 , query_row3 , query_glass3 = 100000009 , 33 , 17

a = Solution()
print(a.champagneTower(poured1 , query_row1 , query_glass1))
print(a.champagneTower(poured2 , query_row2 , query_glass2))
print(a.champagneTower(poured3 , query_row3 , query_glass3))