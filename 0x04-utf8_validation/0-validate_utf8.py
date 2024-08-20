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
        if 0 <= num <= 255:  # Valid range of a byte
            intsInBin.append('{0:08b}'.format(num))
        else:
            return False

    n = len(intsInBin)
    i = 0
    expected_continuation_bytes = 0

    while i < n:
        byte = intsInBin[i]
        if expected_continuation_bytes > 0:
            if byte.startswith('10'):
                expected_continuation_bytes -= 1
            else:
                return False  # Expected continuation byte but didn't get one
        else:
            if byte.startswith('0'):  # 1-byte character
                pass
            elif byte.startswith('110'):  # 2-byte character
                expected_continuation_bytes = 1
            elif byte.startswith('1110'):  # 3-byte character
                expected_continuation_bytes = 2
            elif byte.startswith('11110'):  # 4-byte character
                expected_continuation_bytes = 3
            else:
                return False  # Invalid start byte for a multi-byte character

        i += 1

    return expected_continuation_bytes == 0  # Check if all continuation bytes were found
