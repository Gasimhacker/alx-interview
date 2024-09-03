#!/usr/bin/python3
"""A module to solve the problem of the prime game winner"""


def SieveOfEratosthenes(n):
    """Find the prime numbers up from 0 to n"""
    prime = [True for i in range(n+1)]
    primes_array = [0 for i in range(n+1)]
    p = 2
    num_primes = 0
    for p in range(2, n + 1):
        if (prime[p]):
            num_primes += 1
            for i in range(p * p, n+1, p):
                prime[i] = False
        primes_array[p] = num_primes
    return (primes_array)


def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if not x or not nums or x < 0:
        return None

    Maria_num_wins = 0
    Ben_num_wins = 0
    max_num = max(nums[0:x])
    primes_arr = SieveOfEratosthenes(max_num)

    for i in range(x):
        num_primes = primes_arr[nums[i]]
        if (num_primes % 2):
            Maria_num_wins += 1
        else:
            Ben_num_wins += 1

    if (Maria_num_wins > Ben_num_wins):
        return 'Maria'
    if (Ben_num_wins > Maria_num_wins):
        return 'Ben'
