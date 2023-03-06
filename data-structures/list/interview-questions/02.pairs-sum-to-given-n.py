"""
Find and print the pairs which sum is equal to given n
restrictions: (3,3) , (3,4) & (4,3)
"""


def get_pairs(arr, n):
    pairs = []
    arr = list(set(arr))  # remove duplicates
    # slower arr = [x for i, x in enumerate(arr) if x not in arr[:i]]

    for i in range(len(arr)):
        current_num = arr[i]
        for j in range(i + 1, len(arr)):
            if current_num + arr[j] == n:
                pairs.append((current_num, arr[j]))

    return pairs


arr = [2, 1, 3, 0, 3, 4, 5]
n = 6
pairs = get_pairs(arr, n)
print(pairs)  # [(1, 5), (2, 4)]
