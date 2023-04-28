def num_fact(n, dp):
    if n not in dp:
        rec1 = num_fact(n - 1, dp)
        rec2 = num_fact(n - 3, dp)
        rec3 = num_fact(n - 4, dp)
        dp[n] = rec1 + rec2 + rec3
    return dp[n]


def bot_up_approach(n):
    tb = [1, 1, 1, 2]
    for i in range(4, n + 1):
        tb.append(tb[i - 1] + tb[i - 3] + tb[i - 4])
    print(tb[n])


dp = {0: 1, 1: 1, 2: 1, 3: 2}
n = 4
n2 = 6
print('top down memoization', num_fact(n, dp), num_fact(n2, dp))
bot_up_approach(n)
bot_up_approach(n2)
