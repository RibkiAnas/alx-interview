#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    if total < 1:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total == 0:
            return num_coins
        num_coins += total // coin
        total %= coin

    return num_coins if total == 0 else -1
