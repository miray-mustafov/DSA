def fib(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


memo = dict()
n = 8
print(fib(n, memo))  # 13
