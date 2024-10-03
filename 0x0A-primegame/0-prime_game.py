#!/usr/bin/python3
"""
prime game
"""


def SieveOfEratosthenes(n):
    """
    Sieve of Eratosthenes
    algorithm
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes


def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0
    max_num = max(nums)

    if max_num < 2:  # If no prime numbers exist
        return 'Ben'

    primes = SieveOfEratosthenes(max_num)

    for n in nums:  # Iterate over the rounds
        if n < 2:  # Check for rounds where n is less than 2
            ben_wins += 1
            continue

        prime_count = sum(primes[:n + 1])

        if prime_count % 2 == 0:  # Even prime count means Ben wins
            ben_wins += 1
        else:  # Odd prime count means Maria wins
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None  # If it's a tie
