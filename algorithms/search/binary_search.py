import math


def binarySearch(arr, value):
    start = 0
    end = len(arr) - 1
    middle = math.floor(start + end / 2)

    while not arr[middle] == value:
        if value < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
        if start > end:
            return 'Not found'
    return middle


my_arr = [8, 9, 12, 15, 17, 19, 20, 21, 28]
searched_value = 28
print(f'index of value {searched_value}:', binarySearch(my_arr, searched_value))
