import math


def binary_search(arr, value):  # my_recursive binary search
    start = 0
    end = len(arr) - 1
    middle = math.floor(start + end / 2)

    if value == arr[middle]:
        return middle

    if value < arr[middle]:
        return binary_search(arr[start:middle], value)

    return binary_search(arr[middle + 1::], value)


my_arr = [8, 9, 12, 15, 17, 19, 20, 21, 28]
searched_value = 28
print(f'index of value {searched_value}:', binary_search(my_arr, searched_value))

# while not arr[middle] == value:
#     if value < arr[middle]:
#
