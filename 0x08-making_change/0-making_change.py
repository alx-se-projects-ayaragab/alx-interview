#!/usr/bin/python3
"""
makeChange
"""


def makeChange(coins, total):
    """
    makeChange
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for money in range(1, total + 1):
        for coin in coins:
            if coin <= money:
                dp[money] = min(dp[money], dp[money - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
