"""
Given 2D list calculate the sum of diagonal elements.
"""


def sumDiagonal(listt):
    sum = 0
    for i in range(len(listt)):
        sum += listt[i][i]

    print(sum)


myList2D = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

sumDiagonal(myList2D)  # 15
