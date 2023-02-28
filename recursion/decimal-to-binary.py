"""the first remainder we obtain corresponds to the rightmost bit of the binary number,
 while the last remainder we obtain corresponds to the leftmost bit of the binary number.
 This is because we start with the least significant bit (the rightmost bit) of the binary number
 and work our way towards the most significant bit (the leftmost bit)."""


def to_binary(num):
    if num == 1:
        return 1
    return f'{to_binary(num // 2)}' + f'{num % 2}'


num = 13
from_calculator = 1101
result = to_binary(num)

print(result)
print('valid:', f'{from_calculator}' == result)
# 1x23 + 1x22 + 0x21 + 1x20
# 1x8 + 1x4 + 0x2 + 1x1 = 8 + 4 + 0 + 1 = 13