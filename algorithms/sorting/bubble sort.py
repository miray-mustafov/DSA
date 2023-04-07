def bubble_sort(arr):  # ascending
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [2, 9, 5, 7, 1, 4, 3, 6, 8]
bubble_sort(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
