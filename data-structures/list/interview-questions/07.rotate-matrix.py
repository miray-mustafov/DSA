"""Given matrix with numbers: rotate the matrix(square) to the right 90 degrees
u can extend later for left or more degrees
hints: recursion, layers"""


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def rotate_matrix(matrix, layer=0):
    for i in range(layer, len(matrix) - 1 - layer):
        top = matrix[layer][i]
        right = matrix[i][-1 - layer]
        bot = matrix[-1 - layer][-1 - i]
        left = matrix[-1 - i][layer]

        matrix[i][-1 - layer] = top  # right becomes top
        matrix[-1 - layer][-1 - i] = right  # bot becomes right
        matrix[-1 - i][layer] = bot  # left becomes bot
        matrix[layer][i] = left  # top becomes left
    if len(matrix) - layer > 3:
        rotate_matrix(matrix, layer + 1)


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
