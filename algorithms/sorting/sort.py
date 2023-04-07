def bubble_sort(arr):  # ascending
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i + 1
        for j in range(2 + i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    pass


arr = [2, 9, 5, 7, 1, 4, 3, 6, 8]
print('buble:', bubble_sort(arr.copy()))
print('selection:', selection_sort(arr.copy()))
print('insertion:', insertion_sort(arr.copy()))
