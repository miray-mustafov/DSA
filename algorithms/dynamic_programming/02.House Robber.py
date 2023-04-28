from collections import deque


def houseRobber(houses, hi, memo):
    if hi >= len(houses):
        return 0
    if hi not in memo:
        stealFirstHouse = houses[hi] + houseRobber(houses, hi + 2, memo)
        skipFirstHouse = houseRobber(houses, hi + 1, memo)
        memo[hi] = max(stealFirstHouse, skipFirstHouse)
    return memo[hi]


def bottom_up(houses, start_hi):
    tb = [0] * (len(houses) + 2)
    for hi in range(len(houses) - 1, start_hi - 1, -1):
        tb[hi] = max(houses[hi] + tb[hi + 2], tb[hi + 1])
    return tb[start_hi]


memo = {}
houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0, memo))  # 41
print(bottom_up(houses, 0))  # 41
