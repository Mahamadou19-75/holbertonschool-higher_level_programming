#!/usr/bin/python3
def pow(a, b):
    """Compute a to the power of b"""
    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    elif b < 0:
        for _ in range(-b):
            result *= a
        result = 1 / result
    # b == 0
    return result

