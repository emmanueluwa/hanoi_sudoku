## Hanoi Sudoku Solver

Using recursion and backtracking to check if a sudoku puzzle is unsolvable.

# Sudoku Solver using Recursion

## Overview

This project is a Python implementation of a Sudoku solver using recursion. Sudoku is a popular number-placement puzzle where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that make up the grid contain all of the digits from 1 to 9.

## Purpose

The purpose of this project is to demonstrate the use of recursion in solving problems which involve repetitive steps to find the solution. Recursion is employed to explore possible solutions by making guesses and backtracking when a guess is invalid.

## Components

### `find_empty`

This function identifies the next empty spot (represented by -1) in the Sudoku puzzle. It returns a tuple of the row and column indices of the empty spot or `(None, None)` if there are no more empty spots.

for example:

```
[[-1,  1,  5, ...],
 [-1, -1, -1, ...],
 [ 6, -1, -1, ...]
 ...]
 ```

 represents

```
 -----------
|     1   5 | ...
|           | ...
| 6         | ...
 -----------
 ...

 ```

### `is_valid`

The `is_valid` function checks whether a guess at a specific row and column is valid according to Sudoku rules. It verifies the guess against the values in the corresponding row, column, and 3x3 subgrid.

### `validate_puzzle`

The main solving function, `validate_puzzle`, uses recursion to fill in the Sudoku puzzle. It starts by finding an empty spot, making a valid guess, and then recursively calling itself with the updated puzzle until a solution is found or backtracking is required.

## Usage

To use the Sudoku solver, create a Sudoku puzzle represented as a 9x9 list of lists, where empty spots are denoted by -1. Then, call the `validate_puzzle` function with the puzzle as an argument. If a solution exists, the puzzle will be mutated to the solved state.

Example:

```
example_board = [
    [ 3,  9, -1,  -1,  5, -1,  -1, -1, -1 ],
    [-1, -1, -1,   2, -1, -1,  -1, -1,  5 ],
    [-1, -1, -1,   7,  1,  9,  -1,  8, -1 ],

    [-1,  5, -1,  -1,  6,  8,  -1, -1, -1 ],
    [ 2, -1,  6,  -1, -1,  3,  -1, -1, -1 ],
    [-1, -1, -1,  -1, -1, -1,  -1, -1,  4 ],

    [ 5, -1, -1,  -1, -1, -1,  -1, -1, -1 ],
    [ 6,  7, -1,   1, -1,  5,  -1,  4, -1 ],
    [ 1, -1,  9,  -1, -1, -1,   2, -1, -1 ]
]

```
