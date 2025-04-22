#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    """
    n = len(boxes)
    opened = set([0])     # Start with box 0 as opened
    stack = [0]           # Start exploring from box 0

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key < n and key not in opened:
                opened.add(key)
                stack.append(key)

    # Check if all boxes were opened
    return len(opened) == n

