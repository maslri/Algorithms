# https://leetcode.com/problems/champagne-tower/description/?envType=daily-question&envId=2023-09-24

class Solution:

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float :
        dic = self.populateDefultDict()

        row = 0
        column = 0
        while poured :
            for per_column in range(0, column) :
                if dic[(row, per_column)]["value"] != 1 :
                    dic[(row, per_column)]["value"] += 0.5 ** row
                else :
                    row += 1
                    dic[dic[(row - 1, per_column)]["next1"]]["value"] += 0.5 ** row
                    dic[dic[(row - 1, per_column)]["next2"]]["value"] += 0.5 ** row


        return dic[(query_row, query_glass)]["value"]

    def populateDefultDict(self) -> dict:
        dic = {}
        for row in range(0, 100) :
            for column in range(0, 100) :
                dic[(row, column)] =  { "value" : 0, "next1" : (row + 1, column), "next2" : (row + 1, column + 1)}
        return dic
    
    def doPoured(self, dic : dict, row, per_column) -> dict:
        for per_column in range(0, column) :
                if dic[(row, per_column)]["value"] != 1 :
                    dic[(row, per_column)]["value"] += 0.5 ** row
                else :
                    row += 1
                    dic[dic[(row, per_column)]["next1"]]["value"] += 0.5 ** row
                    dic[dic[(row, per_column)]["next2"]]["value"] += 0.5 ** row
                    row = 0
        

class Solution2:
    
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize a 2D array to represent the glasses
        glasses = [[0.0] * (query_row + 1) for _ in range(query_row + 1)]
        # Pour the initial amount of champagne into the top glass
        glasses[0][0] = poured
        # Simulate the flow of champagne from top to bottom
        for row in range(query_row):
            for glass in range(row + 1):
                excess = (glasses[row][glass] - 1) / 2.0
                if excess > 0:
                    glasses[row + 1][glass] += excess
                    glasses[row + 1][glass + 1] += excess
        # Ensure the value is between 0 and 1 (no more than one glass worth)
        return min(1.0, glasses[query_row][query_glass])

poured1 = query_row1 = query_glass1 = 1
poured2 , query_row2 , query_glass2 = (3 , 1 , 1)
poured3 , query_row3 , query_glass3 = (100000009 , 33 , 17)

a = Solution2()
#print(a.champagneTower(poured1 , query_row1 , query_glass1))
print(a.champagneTower(poured2 , query_row2 , query_glass2))
print(a.champagneTower(poured3 , query_row3 , query_glass3))