class Item:
    def __init__(self, profit, weight, name):
        self.profit = profit
        self.weight = weight
        self.name = name

    def __repr__(self):
        return str(f'{self.name} w{self.weight} p{self.profit}')


def zoKnapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity - items[currentIndex].weight,
                                                          currentIndex + 1)
        a = 2
        profit2 = zoKnapsack(items, capacity, currentIndex + 1)
        a = 2
        return max(profit1, profit2)
    else:
        return 0


mango = Item(31, 3, 'Mango')
apple = Item(26, 1, 'Apple')
orange = Item(17, 2, 'Orange')
banana = Item(72, 5, 'Banana')

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0))
