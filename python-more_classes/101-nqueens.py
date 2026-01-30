#!/usr/bin/python3
"""
Solves the N queens problem
"""
import sys


def print_solution(solution):
    """Prints a solution in the required format"""
    result = []
    for row, col in enumerate(solution):
        result.append([row, col])
    print(result)


def is_safe(solution, row, col):
    """Check if a queen can be placed at (row, col)"""
    for r in range(row):
        c = solution[r]
        if c == col:
            return False
        if abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, solution):
    """Backtracking solver"""
    if row == n:
        print_solution(solution)
        return

    for col in range(n):
        if is_safe(solution, row, col):
            solution[row] = col
            solve_nqueens(n, row + 1, solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution = [-1] * n
    solve_nqueens(n, 0, solution)


if __name__ == "__main__":
    main()
