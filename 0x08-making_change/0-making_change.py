#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    if total < 1:
        return 0

    coins.sort(reverse=True)
    dp = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
