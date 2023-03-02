# x^n = x*x*x*x (n-times)
def pow(x, n):
    assert n == int(n), 'Exponent must be whole num'
    if n == 0:
        return 1
    if n < 0:
        return 1/x * pow(x, n + 1)

    return x * pow(x, n - 1)


print(pow(3, -2))
