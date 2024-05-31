#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    s = []
    if n <= 0:
        return s
    s = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(s[i - 1]) - 1):
            curr = s[i - 1]
            temp.append(s[i - 1][j] + s[i - 1][j + 1])
        temp.append(1)
        s.append(temp)
    return s
