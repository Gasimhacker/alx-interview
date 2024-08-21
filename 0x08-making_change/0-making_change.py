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
    coins = sorted(coins, reverse=True)
    i = 0
    num_coins = 0
    n = len(coins)
    while total > 0:
        if i >= n:
            return -1
        elif total >= coins[i]:
            total -= coins[i]
            num_coins += 1
        else:
            i += 1
    return num_coins
