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


def calculate_coin_ways(amount, coins, coins_now=[]):
    if sum(coins_now) == amount:
        yield coins_now
    elif sum(coins_now) > amount:
        pass
    elif coins == []:
        pass
    else:
        for solution in calculate_coin_ways(amount, coins, coins_now + [coins[0]]):
            yield solution
        for solution in calculate_coin_ways(amount, coins[1:], coins_now):
            yield solution

coins = [1, 2, 3]
amount = 2

solutions = [s for s in calculate_coin_ways(amount, coins)]
print 'Using values %s, there are %s ways to calculate %s such as: ' % (coins, len(solutions), amount)
for s in solutions:
    print s
