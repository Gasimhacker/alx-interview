#!/usr/bin/python3
"""UTF-8 validator"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Check if the data passed is a valid utf-8"""
    i = 0
    data_size = len(data)
    while (i < data_size):
        if (data[i] < 128):
            i += 1
            continue
        num_bytes = 1
        mask = (1 << 6)
        while (data[i] & mask):
            num_bytes += 1
            mask >>= 1
        if (num_bytes < 2 or num_bytes > 4 or num_bytes + i > data_size):
            return (False)
        num_bytes += i
        i += 1
        while (i < num_bytes):
            if (data[i] < 128 or data[i] > 192):
                return (False)
            i += 1
    return (True)
