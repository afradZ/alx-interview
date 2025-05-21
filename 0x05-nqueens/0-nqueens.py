#!/usr/bin/env python3
"""Solves the N-Queens puzzle."""
import sys


def is_safe(row, col, solution):
    """Check if a queen can be placed at (row, col)."""
    for r, c in solution:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(n, row=0, solution=[]):
    """Recursively solve the N-Queens problem."""
    if row == n:
        print(solution)
        return

    for col in range(n):
        if is_safe(row, col, solution):
            solve_nqueens(n, row + 1, solution + [[row, col]])


def validate_args():
    """Validate and extract the input N from command-line arguments."""
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

    return n


if __name__ == "__main__":
    N = validate_args()
    solve_nqueens(N)

