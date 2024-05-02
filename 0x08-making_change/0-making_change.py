#!/usr/bin/python3
"""
A function that returns the minimum number of
coins to make change for a given total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    change = 0
    for coin in coins:
        while total - coin >= 0:
            total -= coin
            change += 1
    if total != 0:
        return -1
    return change
