#!/usr/bin/python3
"""A module that solves the N Queens puzzle"""
from sys import argv, exit


if (len(argv) != 2):
    print('Usage: nqueens N')
    exit(1)

arg = argv[1]

if (not arg.isdigit()):
    print('N must be a number')
    exit(1)

N = int(arg)

if (N < 4):
    print('N must be at least 4')
    exit(1)


def solveNQueens(n):
    """Solve the N queens problem for n x n chess board"""
    board = [[0] * n for _ in range(n)]
    pos_diag = set()
    neg_diag = set()
    cols = set()

    def backtrack(r):
        if (r == n):
            res = []
            [[res.append(c) for c in r if c] for r in board]
            print(res)
            return
        for c in range(n):
            if (c in cols or (r - c) in pos_diag
                    or (r + c) in neg_diag):
                continue

            board[r][c] = [r, c]
            pos_diag.add(r - c)
            neg_diag.add(r + c)
            cols.add(c)
            backtrack(r + 1)
            pos_diag.remove(r - c)
            neg_diag.remove(r + c)
            cols.remove(c)
            board[r][c] = 0
        return
    backtrack(0)


solveNQueens(N)
