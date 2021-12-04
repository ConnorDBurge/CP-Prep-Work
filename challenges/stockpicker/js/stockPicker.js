const picker = (prices) => {
    let dates = []
    let largestProfit = 0
    for (let i = 0; i < prices.length; i++) {
        for (let j = i; j < prices.length; j++) {
            if (prices[j] - prices[i] > largestProfit) {
                largestProfit = prices[j] - prices[i]
                dates = [i, j]
            }
        }
    }
    return dates
}

module.exports = { picker }