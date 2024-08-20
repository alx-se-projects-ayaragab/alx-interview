#!/usr/bin/python3
"""
 a method that determines if a given data
 set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    n = len(data)
    i = 0

    while i < n:
        # Get the binary representation of the byte, formatted to 8 bits
        byte = format(data[i], '08b')

        # Determine how many continuation bytes should follow
        if byte.startswith('0'):
            # 1-byte character (ASCII)
            i += 1
            continue
        elif byte.startswith('110'):
            num_continuation_bytes = 1
        elif byte.startswith('1110'):
            num_continuation_bytes = 2
        elif byte.startswith('11110'):
            num_continuation_bytes = 3
        else:
            # Invalid start byte
            return False

        # Check the next num_continuation_bytes for validity
        for _ in range(num_continuation_bytes):
            i += 1
            if i >= n:
                return False
            continuation_byte = format(data[i], '08b')
            if not continuation_byte.startswith('10'):
                return False

        # Move to the next byte after processing the current character
        i += 1

    return True
