#!/usr/bin/python3
"""
A script that determines the fewest number of coins needed to meet a given
amount total
"""

def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total.

    Args:
        coins: A list of coin denominations
        total: The target amount to be met.

    Returns:
        The fewest number of coins needed, or -1 if the total cannot be met.
    """

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    return dp[total] if dp[total] != float('inf') else -1
