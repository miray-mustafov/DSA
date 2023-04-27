def findMinCost(twoDList, row, col):
    if row == -1 or col == -1:
        return float('inf')
    if row == 0 and col == 0:
        return twoDList[0][0]
    op1 = findMinCost(twoDList, row - 1, col)
    op2 = findMinCost(twoDList, row, col - 1)
    return min(op1, op2) + twoDList[row][col]


twoDList = [[4, 7, 8, 6, 4],
            [6, 7, 3, 9, 2],
            [3, 8, 1, 2, 4],
            [7, 1, 7, 3, 7],
            [2, 9, 8, 9, 3],
            ]
last_row = len(twoDList) - 1
last_col = len(twoDList[0]) - 1
print(findMinCost(twoDList, last_row, last_col))
