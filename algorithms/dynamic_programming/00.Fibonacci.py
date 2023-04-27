def fib(n, memo):  # Top down with memoization recursive
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def fib_tabulation(n):  # Bottom up with tabulation iterative
    tb = [0, 1]
    for i in range(2, n + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[n - 1]


memo = dict()
n = 8
print(fib(n, memo))  # 13
print(fib_tabulation(8))  # 13
