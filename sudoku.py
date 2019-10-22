"""Solve a sudoku from a file and print the solved puzzle to the console

Uses the Sherlock Holmes method of deduction: "Once you eliminate the
impossible, whatever remains, no matter how improbable, must be the truth."
This script keeps track of all possibilities for each cell on the board and
by process of elimination, finds what can not be possible. Once a cell only
has one possible number, the script removes that number from the rest of the
row, column, and square. 

Input: a file named "sudoku clues.txt"
    example format: 53xx7xxxx
                    6xx195xxx
                    x98xxxx6x
                    8xxx6xxx3
                    4xx8x3xx1
                    7xxx2xxx6
                    x6xxxx28x
                    xxx419xx5
                    xxxx8xx79

Output: prints the solved sudoku board to the console
"""

from math import floor

# Create board. Board is a 2-D array. Elements are a list of possible numbers.
board = []
# Board has 9 rows
for i in range(0,9):
    row = []
    # Board has 9 columns
    for j in range(0,9):
        # Initialize cells to all numbers 1-9
        row.append(list(range(1,10)))
    board.append(row)

# Get the clues from a file
text = open("sudoku clues.txt", 'r').read()
clues = text.split("\n")

# Fill board with clues
for i in range(0,9): # Board has 9 rows
    for j in range(0,9): # Board has 9 columns
        if clues[i][j] != 'x':
            board[i][j] = [int(clues[i][j])] # Format as a list of 1 int for now

# Go through the board. Each element is a list of possible numbers. If we've
# reduced a list down to 1 possibility, remove that number from the row, column,
# and square. Also make the 1-element list into an int so we know this cell
# has already been solved.
running = True
while running:
    running = False

    # Find all instances where a cell on the board is a list of 1 integer
    for i in range(0,9):
        for j in range(0,9):
            # If this element is an int, ignore it
            if type(board[i][j]) == int:
                continue
            # Else, it's a list. If it only has 1 element, remove that
            # possibility from the row, column, and square
            elif len(board[i][j]) == 1:

                # Variable inits for this loop
                foundInt = board[i][j][0]
                board[i][j] = foundInt # Change this cell from list to int
                running = True # Flag to keep running

                # Remove int from entire row and entire column
                for k in range(0,9):
                    # Remove from row
                    if type(board[i][k]) == list: # Check that it's a list
                        if foundInt in board[i][k]: # Check that foundInt is in the list
                            board[i][k].remove(foundInt)

                    # Remove from column if it's still there
                    if type(board[k][j]) == list: # Check that it's a list
                        if foundInt in board[k][j]: # Check that foundInt is in the list
                            board[k][j].remove(foundInt)

                # Remove int from entire square
                squareRow = floor(i/3)
                squareCol = floor(j/3)
                for k in range(0,3):
                    for l in range(0,3):
                        # Remove int from square if it's still there
                        if type(board[3*squareRow+k][3*squareCol+l]) == list: # Check if list
                            # Check that foundInt is in the list
                            if foundInt in board[3*squareRow+k][3*squareCol+l]:
                                board[3*squareRow+k][3*squareCol+l].remove(foundInt)

    # Find all instances where one number only appears once in the
    # possibilities of a row
    if not running: # Only run this if needed (because efficiency)
        for i in range(0,9): # Rows
            joinedPossibilities = []
            for j in range(0,9): # Columns
                if type(board[i][j]) == list:
                    joinedPossibilities += board[i][j]
            for k in range(1,10): # integers 1-9
                # If only one cell contains this integer,
                # that cell is this integer
                kCount = joinedPossibilities.count(k)
                if kCount == 1:
                    for j in range(0,9): # Columns again
                        if type(board[i][j]) == list: # Check if list
                            if k in board[i][j]: # Check if k in list
                                board[i][j] = [k]
                                running = True # Flag to keep running

    # Find all instances where one number only appears once in the
    # possibilities of a column
    if not running: # Only run this if needed (because efficiency)
        for i in range(0,9): # Columns
            joinedPossibilities = []
            for j in range(0,9): # Rows
                if type(board[j][i]) == list:
                    joinedPossibilities += board[j][i]
            for k in range(1,10): # integers 0-8
                # If only one cell contains this integer, that cell is this integer
                kCount = joinedPossibilities.count(k)
                if kCount == 1:
                    for j in range(0,9): # Columns again
                        if type(board[j][i]) == list: # Check if list
                            if k in board[j][i]: # Check if k in list
                                board[j][i] = [k]
                                running = True # Flag to keep running

    # Find all instances where one number only appears once in the
    # possibilities of a square
    if not running: # Only run this if needed (because efficiency)
        for i in range(0,3): # Rows
            for j in range(0,3): # Columns
                joinedPossibilities = []
                for m in range(0,3): # Rows
                    for n in range(0,3): # Columns
                        if type(board[3*i+m][3*j+n]) == list:
                            joinedPossibilities += board[3*i+m][3*j+n]
                for k in range(1,10): # integers 1-9
                    # If only one cell contains this integer, that cell is this integer
                    kCount = joinedPossibilities.count(k)
                    if kCount == 1:
                        for m in range(0,3): # Rows again
                            for n in range(0,3): # Columns again
                                if type(board[3*i+m][3*j+n]) == list: # Check if list
                                    if k in board[3*i+m][3*j+n]: # Check if k in list
                                        board[3*i+m][3*j+n] = [k]
                                        running = True # Flag to keep running
                                            # Much nesting. Such loop. Very wow!

# Print solved board
for row in board:
    print(' '.join(str(x) for x in row))
