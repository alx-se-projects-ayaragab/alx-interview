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
        if num in range(1, 256):
            intsInBin.append('{0:08b}'.format(num))
        else:
            return False
    startsWith = ['0', '110', '1110', '11110', '10']
    n = len(intsInBin)
    i = 0
    for bnum in intsInBin:
        for s in startsWith:
            if bnum.startswith(s):
                if s == '0':
                    i += 1
                    continue
                elif s == '10':
                    return False
                else:
                    l = len(s) - 1
                    for _ in range(l):
                        if i + 1 < n and intsInBin[i + 1].startswith('10'):
                            i += 1
                            continue
                        else:
                            return False
    return True
