#!/usr/bin/python3
"""
 a method that determines if a given data
 set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    if not data:
        return True
    intsInBin = []
    for num in data:
        if 255 >= num >= 0:
            intsInBin.append('{0:08b}'.format(num))
        else:
            return False
    n = len(intsInBin)
    i = 0
    continuation_bytes = 0
    while i < n:
        byte = intsInBin[i]
        if byte.startswith('0'):
            i += 1
            continue
        elif byte.startswith('110'):
            continuation_bytes = 1
        elif byte.startswith('1110'):
            continuation_bytes = 2
        elif byte.startswith('11110'):
            continuation_bytes = 3
        else:
            return False
        for _ in range(continuation_bytes):
            i += 1
            if i >= n or not intsInBin[i].startswith('10'):
                return False
        i += 1
    return True
