def find_empty(puzzle):
    """
    finds the next row, col on the puzzle that is not filled
    empty spots are represented as -1

    (row, column) tuple is returned or None
    """

    # 0-8 will be used for the index
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    
    return None, None # no spaces left e.g no -1


def is_valid(puzzle, guess, row, col):
    #check whether guess at paticular row/column is valid
    #return True if valid, return False if not valid
    
    #start with row, easiest since every list in puzzle represents a row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    

    # columns
    col_vals = []
    #go through all rows
    for i in range(9):
        col_vals.append(puzzle[i][col])    ##as list comprehension, col_vals = [puzzle[i][col] for i in range(9)]
    
    if guess in col_vals:
        return False
    
    #checking 3x3 square grid
    #find where the 3x3 square starts, the iterate
    row_start = (row // 3) * 3 # answer will lead to 0, 1, 2 * 3 to get index
    col_start = (col // 3) * 3

    # iterare 3 rows
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if puzzle[row][col] == guess:
                return False

    # if no False returned then guess is valid
    return True



def validate_puzzle(puzzle):
    """
    the puzzle is a list of lists
    each inner list is a row in the sudoku puzzle
    return whether or not a solution exists
      -  if solution exits mutate puzzle to be the solution
    """
    row, col = find_empty(puzzle)

    # only valid inputs allowed so if no spaces left problem is solved
    if row is None:
        return True

    #if there is a space, make a guess between 1 and 9
    for guess in range(1, 10):
        #check if guess is valid
        if is_valid(puzzle, guess, row, col):
            #if guess valid, place guess on that row, col (mutate)
            puzzle[row][col] = guess

            #now recursively call the function with the new (mutated) puzzle
            if validate_puzzle(puzzle):
                return True

    #the solution may not be valid Or guess was not valid
    # BACKTRACK reset and move onto the next guess(try a new number)
    puzzle[row][col] = -1 #resetting value at row,col

    #if none of the numbers we try work, puzzle is unsolvable
    return False


if __name__ == "__main__":
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(validate_puzzle(example_board))
    print("\n")
    print("*******************")
    print("\n")
    print(example_board)
