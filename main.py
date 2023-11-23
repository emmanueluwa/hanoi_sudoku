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
