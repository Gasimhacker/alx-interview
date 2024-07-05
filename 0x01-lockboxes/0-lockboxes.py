#!/usr/bin/python3
"""
This module solves the lockboxes problem
"""
from collections import deque


def canUnlockAll(boxes):
    """Check if you can unlock all boxes

    Args:
        boxes: list[list]: A list of list of keys to other boxes
    Returns:
        True: If you can unlock all boxes
        False: Otherwise
    """
    unlocked = deque([0])
    visited = {0}

    while (unlocked):
        key = unlocked.popleft()
        for locked_key in boxes[key]:
            if locked_key not in visited:
                unlocked.append(locked_key)
                visited.add(locked_key)
        if len(visited) == len(boxes):
            return True
    return False
