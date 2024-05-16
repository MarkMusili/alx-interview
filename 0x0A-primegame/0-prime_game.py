#!/usr/bin/python3
"""
Prime game
"""


def get_primes(n):
    """
    Generate a list of booleans
    where is_prime[i] is True if i is a prime number
    """
    is_prime = [False, False] + [True for _ in range(2, n + 1)]
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def isWinner(x, nums):
    """
    Determine the winner of the game
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        is_prime = get_primes(n)
        primes = is_prime.count(True)
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
