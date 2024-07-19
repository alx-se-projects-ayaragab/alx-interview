#!/usr/bin/python3
"""
log parsing problem
"""

import re

def print_codes(line, codes):
    """
    not to repeat code
    """
    for line in lines:
        print(f'File size: {line[-1]}')
        for k, v in sorted(codes.items()):
            if v != 0:
                print(f'{k}: {v}')


if __name__ == '__main__':
    count = 0
    lines = []
    state_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
    log_pattern = '^(\\d{1,3}\\.){3}\\d{1,3} - \\[\\d{4}-\\d{2}-\\d{2}\\] ' + \
                  '"GET /projects/260 HTTP/1\\.1"' + \
                  ' (200|301|400|401|403|404|405|500) \\d{1,4}$'

    try:
        while True:
            line = input()
            if not re.match(log_pattern, line):
                continue
            line_splitted = line.split(' ')
            state_codes[int(line_splitted[-2])] += 1
            lines.append(line_splitted)
            count += 1
            if count == 10:
                count = 0
                print_codes(lines, state_codes)
                lines.clear()
    except (KeyboardInterrupt, EOFError):
        if lines:
            print_codes(lines, state_codes)
            lines.clear()

    if lines:
        print_codes(lines, state_codes)
