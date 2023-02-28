def to_binary(num):
    if num == 1:
        return 1
    return f'{num % 2}' + f'{to_binary(num // 2)}'


# must be 1010001110101
print(to_binary(5237))
