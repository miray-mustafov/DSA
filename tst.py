def flatten(arr):
    sequence = []
    for el in arr:
        if type(el) is list:
            # sequence.extend(flatten(el))
            sequence = sequence + flatten(el)
        else:
            sequence.append(el)
    return sequence


print(flatten([1, 2, 3, [4, 5]])  # [1, 2, 3, 4, 5]
      )
print(flatten([1, [2, [3, 4], [[5]]]])  # [1, 2, 3, 4, 5]
      )
print(flatten([[1], [2], [3]])  # [1, 2, 3]
      )
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])  # [1, 2, 3]
      )
