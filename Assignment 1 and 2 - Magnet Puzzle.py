## Author : Adeline Soerjonoto
## Combination of Assignment 1 and 2 from unit MCD 4710 Introduction to Algorithms and Programming
## Monash College T3, 2019

import random
import math

### Assignment 1

## Part A - Representation and display ##

# Function name : readBoard
# Input         : fileName
# Output        : positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard 
# Description   : read a file and return all the variable that have been assigned with values from the file  
def readBoard(fileName):
    #Open the file in the parameter
    fileRead = open(fileName, "r")

    #Read the file and assign the value into a variable
    M = int(fileRead.readline().strip())
    N = int(fileRead.readline().strip())
    positivesColumn = listFileRead(fileRead)
    negativesColumn = listFileRead(fileRead)
    positivesRow = listFileRead(fileRead)
    negativesRow= listFileRead(fileRead)
    orientations = listOfListFileRead(fileRead, M)
    workingBoard = listOfListFileRead(fileRead, M)

    #Close the file
    fileRead.close()

    return positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard 

# Function name : listFileRead
# Input         : fileRead
# Output        : 'a list'
# Description   : Read one line in file and split it into list with the data type is int. Return the list
def listFileRead(fileRead):
    return [int(x) for x in fileRead.readline().split()]

# Function name : listOfListFileRead
# Input         : fileRead,M
# Output        : aList
# Description   :
#   Read M lines and return the character in the line one by one with data type string into a list
#   put the list in another list and return the list of list
def listOfListFileRead(fileRead, M):
    aList = []
    for i in range (M):
        aList.append([str(x) for x in fileRead.readline().strip()])
    return aList

# Function name : printBoard
# Input         : positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard
# Output        : 'print the board according to its properties' 
# Description   : display the whole board with all the bars correct according to the orientations and the content 
def printBoard(positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard):
    horzBar = "---"
    vertBar = "|"
    # The Positive Column 
    print ( " + |", end =" ") #the + sign at first
    for posCol in positivesColumn:
        if posCol == -1:
            posCol = " "
        print(posCol,vertBar, end =" ")
    print()
    print(( horzBar + vertBar )* (len(positivesColumn) + 1), end ="") #Horizontal Line
    print(horzBar)
    # The Board
    for row in range (len(positivesRow)):
        # Positive Row
        posRow = str(positivesRow[row])
        if posRow == "-1":
            posRow = " "
        print ( " " + posRow , vertBar , end =" ")
        # Working Board
        for column in range (len(positivesColumn)):
            blockBoard = workingBoard[row][column]
            if blockBoard == 'E':
                blockBoard = " "
            if orientations[row][column] == 'L':#it wilL print space if the orientation is L
                print ( blockBoard + '   ', end ="")
            else :
                print ( blockBoard + ' | ', end ="")
        # Negative Row
        negRow = str(negativesRow[row])
        if negRow == "-1":
            negRow = " "
        print (negRow)
        #Horizontal Line
        print( (horzBar + vertBar ), end ="")
        for col in range (len(positivesColumn)):
            if orientations[row][col] == 'T':
                print ( "   "+ vertBar, end ="") #it wilL print space if the orientation is T
            else :
                print( (horzBar + vertBar ), end ="") 
        print(horzBar)
    #The Negative Column
    print ( "   "+ vertBar, end =" ")
    for negCol in negativesColumn:
        if negCol == -1:
            negCol = " "
        print(negCol, vertBar , end =" ")
    print ("-") #the - sign in the end

## Part B - Helper functions ##

# Function name : canPlacePole
# Input         : row, col, pole, workingBoard
# Output        : 'a Bool' (True or False)
# Description   : checks if it is safe to place one given magnetic block’s pole for a particular coordinates.
def canPlacePole(row, col, pole, workingBoard):
    #Checking the pole
    if pole != '+' and pole != '-': return False
    #Checking the row and col   
    if row > len(workingBoard) or col > len(workingBoard[0]):
        return False
    #Checking the above block 
    if row != 0:
        if workingBoard[row - 1][col] == pole: return False
    #Checking the left block
    if col != 0:
        if workingBoard[row][col - 1] == pole: return False
    #Checking the bottom block
    if row != len(workingBoard)- 1:
        if workingBoard[row + 1][col] == pole: return False
    #Checking the right block
    if col != len(workingBoard[0])-1:
        if workingBoard[row][col + 1] == pole: return False
    return True

# Function name : getBlockOrientation
# Input         : row, col, orientations
# Output        : resultOrientation, oppositeRow, oppositeCol
# Description   : get the orientation of a given slot as well as the coordinates of the other end of the slot, based on the given coordinates of a square and the orientations. 
def getBlockOrientation(row, col, orientations):
    orient = orientations[row][col]
    #For LR Block
    if orient == 'L' or orient == 'R':
        resultOrientation = 'LR'
        oppositeRow = row
        if orient == 'R':
            oppositeCol = col - 1
        else :
            oppositeCol = col + 1
    #For TB Block
    elif orient == 'T' or orient =='B':
        resultOrientation = 'TB'
        oppositeCol = col
        if orient == 'B':
            oppositeRow = row - 1
        else:
            oppositeRow = row + 1
    else:
        print("Invalid Orientation")
    return resultOrientation, oppositeRow, oppositeCol

# Function name : poleCount
# Input         : rowOrCol, index, pole, workingBoard
# Output        : count 
# Description   : finds the total number of positive (+) poles or negative (-) poles in a particular row or column. 
def poleCount(rowOrCol, index, pole, workingBoard):
    count = 0
    #Count pole in row
    if rowOrCol == 'r':
        for col in range (len(workingBoard[index])):
            if workingBoard[index][col]== pole:
                count+= 1
    #Count pole in column
    elif rowOrCol == 'c':
        for row in range (len(workingBoard)):
            if workingBoard[row][index]== pole:
                count+= 1
    else:
        print("Invalid value for rowOrCol")
    return count

# Function name : randomPoleFlip
# Input         : alist, percentage, flipValue
# Output        : -
# Description   : randomly swaps a percentage of elements from alist with the flipValue
def randomPoleFlip(alist, percentage, flipValue) :
    counter = 0
    while counter < int(len(alist) * percentage) : #runs until the number of flipValues in the list is match with the result of calculation
        randIndex = random.randrange(len(alist))
        if alist[randIndex] != flipValue: 
            alist[randIndex] = flipValue
            counter += 1

## Part C -  Board Generation Functions ##

# Function name : orientationsGenerator
# Input         : M,N
# Output        : newOrt
# Description   : randomly generate the orientations as a list of lists for a board of size M x N. 
def orientationsGenerator(M,N):
    newOrt = []
    
    #Create a new orientations with TB 
    for row in range(0,M,2):
        newOrt.append(["T" for x in range(N)])
        newOrt.append(["B" for x in range(N)])

    #Randomize the orientations 
    for counter in range(1000):
        randomOrientations(M,N, newOrt)
        
    return newOrt

# Function name : randomOrientations
# Input         : M,N, newOrt
# Output        : -
# Description   : picking a random block and check whether the orientations can be changed
def randomOrientations(M,N, newOrt):
    #Pick random row and coloumn
    randRow = random.randrange(M)
    randCol = random.randrange(N)

    #Get the orientation and location of the L or T
    randOrt, row, col = getBlockLOrT(randRow, randCol, newOrt)

    #Change two blocks of orientations
    if randOrt == 'LR' :
        if newOrt[row-1][col] == 'L' and row != 0:
            newOrt[row-1][col] = 'T'
            newOrt[row][col] = 'B'
            newOrt[row-1][col+1] = 'T'
            newOrt[row][col+1] = 'B'
    elif randOrt == 'TB' :
        if newOrt[row][col-1] == 'T' and col != 0:
            newOrt[row][col-1] = 'L'
            newOrt[row][col] = 'R'
            newOrt[row+1][col-1] = 'L'
            newOrt[row+1][col] = 'R'
    else:
        print("Invalid Orientation")

# Function name : getBlockLOrT
# Input         : row, col, orientations
# Output        : resultOrientation, blockRow, blockCol
# Description   : get the orientation of a given slot as well as the coordinates of the L or T, based on the given coordinates of a square and the orientations. 
def getBlockLOrT (row, col, orientations):
    orient = orientations[row][col]
    #For LR Block, return L coordinates
    if orient == 'L' or orient == 'R':
        resultOrientation = 'LR'
        blockRow = row
        if orient == 'R':
            blockCol = col - 1
        else :
            blockCol = col
    #For TB Block, return T coordinates
    elif orient == 'T' or orient =='B':
        resultOrientation = 'TB'
        blockCol = col
        if orient == 'B':
            blockRow = row - 1
        else:
            blockRow = row 
    else:
        print("Invalid Orientation")
    return resultOrientation, blockRow, blockCol

# Function name : fillWithMagnets
# Input         : orientations
# Output        : newBoard
# Description   : creates a board that is full of magnet blocks. 
def fillWithMagnets(orientations):
    newBoard =[]
    
    #Create an 'Empty' board (filled with 'E')
    for counter in range(len(orientations)):
        newBoard.append(["E" for col in range(len(orientations[0]))])

    #Fill the board with magnets
    for row in range(len(orientations)):
        for col in range(len(orientations[row])):            
            if canPlacePole(row, col ,'+', newBoard) == True: #check if it can place +, if not put -
                newBoard[row][col] = "+"
            else:
                newBoard[row][col] = "-" 
    return newBoard

# Function name : randomBlankBlocks
# Input         : board, orientations
# Output        : -
# Description   : randomly replace 30% of the blocks with blank blocks (‘X’ blocks)
def randomBlankBlocks(board, orientations):
    counter = 0
    while counter < math.floor(len(board)*len(board[0]) / 2 * 0.30): # run until 0.30 of the block change into 'X' block
        randRow = random.randrange(len(board)) 
        randCol = random.randrange(len(board[0]))
        if board[randRow][randCol] != "X":
            ort, row, col = getBlockLOrT(randRow, randCol, orientations)
            #Change a random block into 'X' block
            if ort == "LR":
                board[row][col] = "X"
                board[row][col+1] = "X"
            else:
                board[row][col] = "X"
                board[row+1][col] = "X"
            counter +=1


# Function name : listNumPole
# Input         : rowOrCol, index, pole, board
# Output        : listPole
# Description   : creates a list of the total number of positive (+) poles or negative (-) poles in a particular row or column.
def listNumPole(rowOrCol, index, pole, board):
    listPole = []
    for counter in range(index):
        listPole.append(poleCount(rowOrCol,counter,pole,board))#put the number of poles in a list
    return listPole

# Function name : randomNewBoard
# Input         : M,N
# Output        : positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard
# Description   : create a new random board of size M x N and return the properties of it
def randomNewBoard (M,N):
    
    orientations = orientationsGenerator(M,N) #create a new random orientaions
    workingBoard = fillWithMagnets(orientations)#create a new random workingBoard
    randomBlankBlocks(workingBoard, orientations)#change some of the magnets into blank

    #Create a list of the total number for poles in each rows and cols
    positivesColumn = listNumPole('c', N, '+', workingBoard) 
    negativesColumn = listNumPole('c', N, '-', workingBoard)
    positivesRow = listNumPole('r', M, '+', workingBoard)
    negativesRow = listNumPole('r', M, '-', workingBoard)

    #Randomly change the value in the list into -1
    flipValue = -1
    percentage = 0.5
    randomPoleFlip(positivesColumn,percentage,flipValue)
    randomPoleFlip(negativesColumn,percentage,flipValue)
    randomPoleFlip(positivesRow,percentage,flipValue)
    randomPoleFlip(negativesRow,percentage,flipValue)
    return positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard

### Assignment 2

## Part A : Helper functions

# Function name : firstEmpty
# Input         : board
# Output        : a number
# Description   : finds the first block that is 'E' (Empty)
def firstEmpty(board):
    for row in range (len(board)):
        for col in range (len(board[0])):
            if board[row][col] == "E": #if the block is empty, it will return the row and the col
                return row, col 
    return -1, -1 # if there is not a block that is empty, it wil return -1 , -1

# Function name : setToBoard
# Input         : set, orientations
# Output        : board
# Description   : takes a given set list and converts it into a board based on existing orientations
def setToBoard(set, orientations):
    board = []
    for counter in range(len(orientations)):
        board.append(["E" for col in range(len(orientations[0]))])
    for x in set:
        row, col = firstEmpty(board) # get the location of the first block that is empty
        if row != -1 and col != -1:
            orientation, opRow, opCol = getBlockOrientation(row, col, orientations) #get the opposite block location
            if x == 0:
                board[row][col] = "+"
                board[opRow][opCol] = "-"
            elif x == 1:
                board[row][col] = "-"
                board[opRow][opCol] = "+"
            else:
                board[row][col] = "X"
                board[opRow][opCol] = "X"
    return board

# Function name : compareList
# Input         : checkLst, lst
# Output        : a Bool (True or False)
# Description   : compares two list whether they are the same or not
def compareList(checkLst, lst):
    for index in range(len(lst)):
        if lst[index] != -1:
            if checkLst[index] != lst[index]: #compare each item 
                return False
    return True

# Function name : poleChecked
# Input         : board
# Output        : a Bool (True or False)
# Description   : checks if there is a pole that is invalid in the board
def poleChecked(board):
    for row in range(len(board)):
        for col in range (len(board)):
            pole = board[row][col]
            if pole != "X":
                if canPlacePole(row, col, pole, board) == False: #check the pole
                    return False
    return True

# Function name : isSolution
# Input         : positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard
# Output        : a Bool (True or False)
# Description   : checks if a given board is a valid solution to the puzzle. The function will return Boolean
#                 value True for valid solutions; otherwise, it will return False. 
def isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard):

    # Get the number of positive poles (+) and negative poles (–)in each row and column of the board 
    checkPositivesColumn = listNumPole('c', len(workingBoard[0]), '+', workingBoard) 
    checkNegativesColumn = listNumPole('c', len(workingBoard[0]), '-', workingBoard)
    checkPositivesRow = listNumPole('r', len(workingBoard), '+', workingBoard)
    checkNegativesRow = listNumPole('r', len(workingBoard), '-', workingBoard)

    # Put the each list into a list
    checkLst=[checkPositivesColumn,checkNegativesColumn,checkPositivesRow,checkNegativesRow]
    lst = [positivesColumn, negativesColumn, positivesRow, negativesRow]

    # Check if the number of positive poles (+) and negative poles (–)in each row and column of the board 
    #  match with positivesColumn, negativesColumn, positivesRow, and negativesRow
    for x in range(4):
        if compareList(checkLst[x],lst[x]) == False: # 
            return False
    # Check if the given board does not violate the orthogonal rule i.e. the magnetic poles are not vertically or
    #  horizontally adjacent. 
    if poleChecked(workingBoard) == False:
        return False
    return True

## Part B : Brute-force

# Function name : decBits
# Input         : dec, bitLength, base
# Output        : bitList
# Description   : convert a decimal number into a bit in a form of a list
def decBits(dec, bitLength, base):
    if bitLength:
        bitList = [0] * bitLength # create the bit list
    k = -1
    while dec>0:
        #calculate the bit 
        bitList[k] = dec%base
        dec = dec//base
        k -= 1
    return bitList

# Function name : subsetListGenerator
# Input         : n, bit
# Output        : subsetList
# Description   : generates all possible subset and return it in a list
def subsetListGenerator(n, bit):
    subsetList = []
    for k in range(bit**n):
        subsetList.append(decBits(k,n, bit)) #append each bit list into a list
    return subsetList

# Function name : bruteforce
# Input         : positivesColumn, negativesColumn, positivesRow, negativesRow, orientations
# Output        : the solution board
# Description   : return the solution to the board once it finds it. 
def bruteforce(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations):
    slot = int(len(orientations)*len(orientations[0])/2) # calculate the number of slots which will determined the lenght of the set
    possibleSolutions = []
    base = 3
    possibleSolutions = subsetListGenerator(slot, base) # create all possible subsets
    for x in range(len(possibleSolutions)):
        aBoard= setToBoard(possibleSolutions[x],orientations) #convert the set into a board
        check = isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, aBoard) #check if it is a solution
        if check == True:
            return setToBoard(possibleSolutions[x],orientations) #return the solution
    print("No Solution")
    return -1



### Output

    
## Assignment 1
        
print("###########    Assignment 1    ###########")
sampleFiles = ["sampleFile1.txt","sampleFile2.txt","sampleFile3.txt","sampleFile4.txt","sampleFile5.txt"]     
#Read a Board from File and Print
for sample in sampleFiles:
    positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard = readBoard(sample) 
    printBoard(positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard)
    print()
#Create New Board and Print 
M = 6
N = 6
positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard = randomNewBoard(M,N)
print()
printBoard(positivesColumn, negativesColumn, positivesRow , negativesRow ,orientations, workingBoard)
print()

## Assignment 2

print("###########    Assignment 2    ###########")
positivesColumn = [-1, -1, -1, -1, -1]
negativesColumn = [-1, -1, -1, -1, -1]
positivesRow = [-1, -1, -1, -1, -1, -1]
negativesRow = [-1, -1, -1, -1, -1, -1]
orientations = [ ['T', 'L', 'R', 'L', 'R'],
 ['B', 'T', 'T', 'L', 'R'],
['T', 'B', 'B', 'T', 'T'],
['B', 'L', 'R', 'B', 'B'],
['L', 'R', 'L', 'R', 'T'],
['L', 'R', 'L', 'R', 'B'] ]
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations,orientations)
set=[0,1,1,0]
workingBoard= setToBoard(set,orientations)
print("###########################################")
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations,workingBoard)
set =[0,2,0,2,1,0,2]
workingBoard= setToBoard(set,orientations)
print("###########################################")
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations,workingBoard)
print("###########################################")
positivesColumn = [1,1,1]
negativesColumn = [1,1,1]
positivesRow = [-1,-1]
negativesRow = [-1,-1]
orientations = [['L', 'R', 'T'],
 ['L', 'R', 'B']]
workingBoard = [['+', '-', '-'],
 ['-', '+', '+']]
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow,orientations, workingBoard)
print(isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow,
orientations, workingBoard))
workingBoard = [['+', '-', '+'],
 ['-', '+', '-']]
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)
print(isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow,
orientations, workingBoard))
print("###########################################")
positivesColumn = [1,1,-1]
negativesColumn = [1,1,-1]
positivesRow = [1,-1]
negativesRow = [-1,-1]
orientations = [['L', 'R', 'T'],
 ['L', 'R', 'B']]
workingBoard = [['+', '-', '+'],
 ['-', '+', '-']]
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow,orientations,workingBoard)
print(isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow,orientations, workingBoard))
workingBoard = [['+', '-', 'X'],
 ['-', '+', 'X']]
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow,orientations,workingBoard)
print(isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow,orientations, workingBoard))
print("###########################################")
positivesColumn = [2, 1, 1, -1, -1]
negativesColumn = [1, -1, -1, 2, 1]
positivesRow = [2, -1, -1, 1]
negativesRow = [1, 3, -1, -1]
orientations = [['T', 'L', 'R', 'L', 'R'],
 ['B', 'L', 'R', 'L', 'R'],
['L', 'R', 'L', 'R', 'T'],
['L', 'R', 'L', 'R', 'B']]
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow,
orientations, orientations)
print("#############################################")
solution=[]
solution = bruteforce(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations)
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, solution)

        





