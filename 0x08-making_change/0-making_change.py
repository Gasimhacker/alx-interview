#!/usr/bin/python3
"""
A module to determine the fewest number
of coins needed to meet
a given amount
"""


def makeChange(coins, total):
    """Find the fewest number of coins needed"""
    if total <= 0:
        return 0
    num_coins = [total + 1] * (total + 1)
    num_coins[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                num_coins[i] = min(num_coins[i], 1 + num_coins[i - coin])
    if num_coins[total] < total + 1:
        return num_coins[total]
    return -1
