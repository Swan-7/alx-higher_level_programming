#!/usr/bin/python3
# 101-nqueens.py
# Brennan D Baraban <375@holbertonschool.com>
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions."""
import sys

def is_safe(board, row, col, n):
    # check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, row, n, solutions):
    if row == n:
        solutions.append([list(row) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, solutions)
            board[row][col] = 0

def n_queens(n):
    solutions = []
    board = [[0] * n for _ in range(n)]
    solve(board, 0, n, solutions)
    return solutions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    n = sys.argv[1]
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = n_queens(n)
    for solution in solutions:
        print(*solution)
