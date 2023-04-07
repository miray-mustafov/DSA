def find_max_num(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max_num(arr, n - 1))


arr = [11, 4, 12, 7]
n = len(arr)
print('Max num:', find_max_num(arr, n))
