"""
You are given an amount of money and a list of coin denominations,
calculate the  number of ways to make that amount with the available coins.

Example:
Input: amount = 4, denominators = [1, 2, 3]
Output: 4, because there are 4 ways to calculate 4 as such:
4 = 1 + 1 + 1 + 1
  = 1 + 1 + 2
  = 1 + 3
  = 2 + 2
"""


def calculate_coin_ways(amount, coins, len_coins):
    # import ipdb; ipdb.set_trace()
    print "AMOUNT: " + str(amount)
    print "COINS: " + str(coins)
    print "LEN_COINS: " + str(len_coins)
    # Negative amount is impossible, 0 ways to do that
    if (amount < 0):
        return 0

    # No coins and amount > 0, 0 ways to do that
    if (len_coins <= 0 and amount > 0):
        return 0

    # Amount == 0, only 1 way (not include any coin) to get the amount
    if (amount == 0):
        return 1

    # Recursive to subdivide in little problems, the result is the sum of the
    # calculation of the cell in the left and the cell above
    cosa1 = calculate_coin_ways(amount, coins, len_coins - 1)
    cosa2 = calculate_coin_ways(amount - coins[len_coins - 1], coins, len_coins)
    print "COSA1: " + str(cosa1)
    print "COSA2: " + str(cosa2)
    return cosa1 + cosa2
    # return calculate_coin_ways(amount, coins, len_coins - 1) + calculate_coin_ways(amount - coins[len_coins - 1], coins, len_coins)


coins = [1, 2, 3]
amount = 4
number_solutions = calculate_coin_ways(amount, coins, len(coins))
print "There are %s ways to calculate %s with %s" % (number_solutions, amount, coins)
