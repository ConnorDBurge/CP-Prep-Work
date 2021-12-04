def picker(prices):
    largest_profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > largest_profit:
                largest_profit = prices[j] - prices[i]
                dates = [i, j]
    return dates
