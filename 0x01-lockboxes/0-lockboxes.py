#!/usr/bin/env python3
"""
Lockboxes quiz
"""


def canUnlockAll(boxes):
    """
    Determines if a box can be opened
    """
    keys = set([0])

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in keys:
                keys.add(key)
                queue.append(key)

    return len(keys) == len(boxes)
