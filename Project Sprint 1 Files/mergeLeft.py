
from turtle import update
import temporaryBoard

boardsize = 4

def mergeoneRowL(row):
    for j in range (boardsize - 1):
        for i in range(boardsize - 1, 0, -1):
            if row [i-1] == 0:
                row [i-1] = row[i]
                row[i] = 0

    for i in range(boardsize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

    for i in range(boardsize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row

def mergeLeft(currBoard):
    for i in range(boardsize):
        currBoard[i] = mergeoneRowL(currBoard[i])

    return currBoard

def returnMergeLeft():
    updatedBoard = mergeLeft(temporaryBoard.boardFill)
    temporaryBoard.display(updatedBoard)

