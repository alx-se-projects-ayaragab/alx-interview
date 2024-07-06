#!/usr/bin/python3
"""
0. Lockboxes interview question
"""


def canUnlockAll(boxes):
    n = len(boxes)
    b_states = [False] * n
    b_states[0] = True
    keys = [0]

    while keys:
        current = keys.pop()
        if boxes[current] != []:
            for key in boxes[current]:
                if key < n and not b_states[key]:
                    b_states[key] = True
                    keys.append(key)
        else:
            b_states[current] = True
    return all(b_states)
