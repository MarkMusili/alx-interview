#!/usr/bin/python3
"""
Mininum operations task
"""


def minOperations(n) -> int:
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n == 1:
        return 0
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

        if dp[i] == i:
            dp[i] = i

    return dp[n]
