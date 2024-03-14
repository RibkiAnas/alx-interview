#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """
    Determine who the winner of the game is
    """
    if not nums or x < 1:
        return None

    prime = [False, False] + [True for _ in range(x - 1)]
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False

    prime = [i for i, j in enumerate(prime) if j]

    n = 0
    for i in nums:
        if i in prime:
            n += 1

    if n % 2 == 0:
        return "Maria"
    return "Ben"
