#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """
    Determine who the winner of the game is
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    sieve = [0, 0] + [1 for _ in range(max_num - 1)]
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = 0

    sieve = [i for i in range(max_num + 1) if sieve[i]]
    wins = {"Maria": 0, "Ben": 0}
    for num in nums:
        primes = sum(i <= num for i in sieve)
        if primes % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
