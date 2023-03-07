"""Given matrix with numbers: rotate the matrix(square) to the right 90 degrees
u can extend later for left or more degrees"""


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def rotate_matrix(matrix):
    for i in range(len(matrix) - 1):
        top = matrix[0][i]
        right = matrix[i][-1]
        bot = matrix[-1][-1 - i]
        left = matrix[-1 - i][0]

        matrix[i][-1] = top  # right becomes top
        matrix[-1][-1 - i] = right  # bot becomes right
        matrix[-1 - i][0] = bot  # left becomes bot
        matrix[0][i] = left  # top becomes left


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_matrix(matrix)

rotate_matrix(matrix)
print_matrix(matrix)

# ---------------------4x4------------------------------
matrix4x4 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
print_matrix(matrix4x4)
rotate_matrix(matrix4x4)
print_matrix(matrix4x4)
