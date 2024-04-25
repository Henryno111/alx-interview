#!/usr/bin/python3
"""
    This code defines a function `minOperations` that calculates the fewest
    number of operations
    needed to achieve a desired number of 'H' characters in a text file with
    only copy and paste operations.

    Args:
    n: The desired number of 'H' characters.

    Returns:
    The minimum number of operations required, or 0 if the
    number is impossible.
"""


def minOperations(n):

    """
    This function uses dynamic programming to solve the
    minimum operations problem.

    Args:
    n: The desired number of 'H' characters.

    Returns:
    The minimum number of operations required,
    for 0 if the number is impossible.
    """

    if n <= 1:
        return 0
    result = n

    # Iterate through all possible factors of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # If i is a factor of n, calculate the number of operations needed
            result = min(result, minOperations(i) + n // i)
            # Also consider the other factor, which is n // i
            result = min(result, minOperations(n // i) + i)

    return result
