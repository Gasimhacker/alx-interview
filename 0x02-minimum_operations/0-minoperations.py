#!/usr/bin/python3
"""
A module to find the fewest number of operations needed to
result in exactly n H characters in a file that contains
a single character H and given that you can execute only
two operations in this file: Copy All and Paste
"""
from math import sqrt


def minOperations(n: int) -> int:
    """
    Find the fewest number of operations needed to
    result in exactly n H characters in a file
    Returns:
        The fewest number of operations needed
    """
    if n <= 0:
        return 0
    res = 0
    while(n % 2 == 0):
        res += 2
        n /= 2
    for i in range(3, int(sqrt(n) + 1), 2):
        while (n % i == 0):
            res += i
            n /= i
    if n > 2:
        res += n
    return int(res)
