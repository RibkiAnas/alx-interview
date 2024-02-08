#!/usr/bin/python3
""" N queens """
import sys


def solve_n_queens(n):
    """" N queens problem """
    def can_place(pos, ocuppied_positions):
        """ Check if a queen can be placed in a position """
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
              ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
              ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(ocuppied_positions, target_row, n):
        """ Place a queen in a row """
        if target_row == n:
            result.append(ocuppied_positions)
            return
        for column in range(n):
            if can_place(column, ocuppied_positions):
                place_queen(ocuppied_positions + [column], target_row + 1, n)

    result = []
    place_queen([], 0, n)
    return result


def print_result(result):
    """ Print the result """
    for res in result:
        print([[i, res[i]] for i in range(len(res))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

print_result(solve_n_queens(n))
