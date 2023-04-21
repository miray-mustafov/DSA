def get_optimal_change(money):
    coins = [1, 2, 5, 10, 20, 50, 100, 1000]
    change = []
    j = len(coins) - 1
    while money > 0:
        for i in range(j, -1, -1):
            if coins[i] <= money:
                change.append(coins[i])
                money -= coins[i]
                j = i
                break
    return change


money = 70
money2 = 2035
money3 = 1
print(get_optimal_change(money))
print(get_optimal_change(money2))
print(get_optimal_change(money3))
