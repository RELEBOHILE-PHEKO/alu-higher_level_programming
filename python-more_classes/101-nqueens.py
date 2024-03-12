#!/usr/bin/python3
"""
N Queens Puzzle Solution
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on the board.
    """
    # Check row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Solve the N Queens puzzle using backtracking.
    """
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0


def nqueens(n):
    """
    Print all solutions to the N Queens puzzle.
    """
    solutions = []
    board = [[0 for j in range(n)] for i in range(n)]
    solve_nqueens(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
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

    solutions = nqueens(n)

    for solution in solutions:
        print(solution)
