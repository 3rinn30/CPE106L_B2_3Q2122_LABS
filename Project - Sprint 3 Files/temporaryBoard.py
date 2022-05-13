# This python program will printout a temporary board for initial run and creation of the Project.
import random

from pyparsing import col

boardSize = 4

def display(boardFill):

    biggest = boardFill[0][0]
    for row in boardFill:
        for element in row:
            if element > biggest:
                biggest = element

    spaces = len(str(biggest))

    for row in boardFill:
        currentRow = "|"
        for element in row:
            if element == 0:
                currentRow += " " * spaces + "|"
            else:
                currentRow += (" " * (spaces - len(str(element)))) + str(element) + "|"
        print(currentRow)
    print()

def newValue():
    if random.randint(1,8) == 1:
        return 2
    else:
        return 2

boardFill = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    boardFill.append(row)

numNeeded = 2
while numNeeded > 0:
    rowNeed = random.randint(0, boardSize - 1)
    colNeed = random.randint(0, boardSize - 1)

    if boardFill[rowNeed][colNeed] == 0:
        boardFill[rowNeed][colNeed] = newValue()
        numNeeded -= 1

def AddValue():
    rowNeed = random.randint(0, boardSize  - 1)
    colNeed = random.randint(0, boardSize - 1)

    while not boardFill[rowNeed][colNeed] == 0:
        rowNeed = random.randint(0, boardSize - 1)
        colNeed = random.randint(0, boardSize - 1)
    
    boardFill[rowNeed][colNeed] = newValue()