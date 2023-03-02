def gcd(n1, n2):
    assert n1 == int(n1) and n2 == int(n2), "Numbers must be integers!"
    if n2 < 0:
        n2 = -1 * n2

    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


num1 = 48
num2 = -18

print('gcd:', gcd(num1, num2))
print(gcd(18, 48))
print(gcd(-18, -48))
print(gcd(17, 48))
print(gcd(32, -32*32))
