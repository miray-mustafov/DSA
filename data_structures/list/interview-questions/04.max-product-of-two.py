"""in all positive integers array, find and return the maximum product of a pair"""

arr = [2, 13, 14, 1, 0, 5, 12, 16]


def get_max_product(arr):
    max_product = 0
    pair = ()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]
                pair = (arr[i], arr[j])

    return max_product, pair


product = get_max_product(arr)
print(product)
