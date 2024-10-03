#!/usr/bin/python3
"""
prime game
"""


def isWinner(x, nums):
    """
    isWinner
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

    if x == 0 or not nums:
        return None
    maria_wins = 0
    ben_wins = 0
    max_num = max(nums)
    primes = SieveOfEratosthenes(max_num)
    for n in nums:
        sumOfP = sum(primes[:n + 1])
        if sumOfP % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    return 'Ben' if ben_wins > maria_wins else 'Maria'
