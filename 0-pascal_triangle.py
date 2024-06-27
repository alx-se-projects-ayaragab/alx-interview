#!/usr/bin/python3
"""
interview prep: pascal triangle
"""
def pascal_triangle(n):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if n <= 0:
        return []
    res = [[1]]
    for _ in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
