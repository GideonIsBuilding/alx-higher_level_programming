#!/usr/bin/python3

"""

This module contains an algorithm that resolves the N-Queen puzzle
using backtracking

"""

import sys


def isSafe(m_queen, nqueen):
    """ Method that determines if the queens can or can't kill each other

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill

    """

    for i in range(nqueen):
        if m_queen[i] == m_queen[nqueen]:
            return False
        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

    return True


def print_result(m_queen, nqueen):
    """ Method that prints the list with the Queens positions

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    """

    res = []

    for i in range(nqueen):
        res.append([i, m_queen[i]])

    print(res)


def Queen(m_queen, nqueen, solution_count):
    """ Recursive function that executes the Backtracking algorithm

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number
        solution_count: count of solutions

    """

    if nqueen == len(m_queen):
        solution_count[0] += 1
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while m_queen[nqueen] < len(m_queen) - 1:
        m_queen[nqueen] += 1
        if isSafe(m_queen, nqueen):
            if nqueen != len(m_queen):
                Queen(m_queen, nqueen + 1, solution_count)


def solveNQueen(size):
    """ Function that invokes the Backtracking algorithm

    Args:
        size: size of the chessboard

    """

    m_queen = [-1 for i in range(size)]
    solution_count = [0]

    Queen(m_queen, 0, solution_count)

    print("Total Solutions:", solution_count[0])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except:
        print("N must be a number\n")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4\n")
        sys.exit(1)

    solveNQueen(size)
