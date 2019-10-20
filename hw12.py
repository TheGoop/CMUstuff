
def areLegalValues(values): 
    s = set(values) #gets rid of uniques 
    c = values.count(0)# counts 0
    if c != 0: #sees if there are zeros, check if set = values in length
        return len(s) == len(values)-c+1
    else:
        return len(s) == len(values)


def isLegalRow(board,r): #is row legaal?
    return areLegalValues(board[r])

def isLegalCol(board, c):
    column = []
    for r in range(len(board)): #iteratates through board and gets col
        column.append(board[r][c])
    return areLegalValues(column)#checks if col is legal

def isLegalBlock(board,n):
    rows = board[(n//3)*3:(n//3)*3 + 3] #gets the rows of the nth square
    block = [] #where the selected block will go
    colIndex = n%3 * 3 #beginning of range of columns of block
    maxColIndex = colIndex + 3 #end of range of columns of block
    for r in rows: #iterates through every row, grabbing the values from the columns needed
        block.append(r[colIndex:maxColIndex])
    oneDBlock = [] #where the values will be stored in 1D form
    for r in block: #iterates through the block
        oneDBlock.extend(r) #adds all values in 1D form
    return areLegalValues(oneDBlock) #checks if the block in one D form is legal
    
def isLegalSudoku(board):
    for r in range(len(board)): #iterates through every row
        if not isLegalRow(board,r): #if row isn't legal, sudoku isn't legal
            return False
    for c in range(len(board)): #iterates through every col
        if not isLegalCol(board,c):#if col isn't legal, sudoku isn't legal
            return False
    for block in range(len(board)): #iterates through every block
        if not isLegalBlock(board,block): #if block isn't legal, sudoku isn't legal
            return False
    return True #returns true if everything is legal



def figureOutBlock(row, col): #figures out block number of value at row and col
    row//=3
    col//=3
    blockBoard = []
    for r in range(3): #creates a board with the block numbers labeled
        lst = []
        for c in range(3*r, 3*r + 3):
            lst.append(c)
        blockBoard.append(lst)
    return blockBoard[row][col] #returns the block number for row and column




def findNextZero(board): #finds next zero
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                return [r,c]

def solveSudoku(board):#wrapper for solve function
    return solve(board)

def solve(board):
    zeroCoords = findNextZero(board) #finds next zero
    if zeroCoords == None: #if no zeros (like a base case) returns board
        return board
    r = zeroCoords[0] #gets row of 0
    c = zeroCoords[1] #gets col of 0
    for num in range(1,len(board)+1): #trys every number possible in sudoku
        board[r][c] = num
        if isLegalRow(board, r) and isLegalCol(board, c) and isLegalBlock(board, figureOutBlock(r,c)): #if value works
            tempBoard = solve(board) #keeps going solving board
            if tempBoard != None: #base
                return tempBoard
        board[r][c] = 0 #resets if value doesnt work
    return None

def testSolveSudoku():
    print('Testing solveSudoku()...', end='')
    board = [
              [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
              [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
              [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
              [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
              [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
              [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
              [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
              [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
              [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
    solved = solveSudoku(board)
    solution = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
               ]
    board = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
               ]
    solved = solveSudoku(board)
    solution = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
               ]
    assert (solved == solution)
    board = [
                [0, 4, 5, 2, 8, 6, 1, 7, 9],
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 0, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 0, 9, 7, 6, 1, 4, 0, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 0, 6, 3, 5]
               ]
    solved = solveSudoku(board)
    solution = [
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5]
               ]
    print('Passed!')

testSolveSudoku()
