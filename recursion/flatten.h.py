"""flatten
Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

Examples

flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
flatten([[1], [2], [3]]) # [1, 2, 3]
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]"""


def flatten(arr):
    sequence = []
    if len(arr) == 0:
        return []
    for el in arr:
        if not isinstance(el, list):
            sequence.append(el)
        else:
            sequence = sequence + flatten(el)
            # sequence.extend(flatten(el))
    return sequence


print(flatten([1, 2, 3, [4, 5]])  # [1, 2, 3, 4, 5]
      )
print(flatten([1, [2, [3, 4], [[5]]]])  # [1, 2, 3, 4, 5]
      )
print(flatten([[1], [2], [3]])  # [1, 2, 3]
      )
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])  # [1, 2, 3]
      )
