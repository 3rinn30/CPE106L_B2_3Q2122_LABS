import transposeBoard
import mergeRight
import temporaryBoard

boardSize = 4

def mergeDown(currBoard):
    currBoard = transposeBoard.transpose(currBoard)
    currBoard = mergeRight.mergeRight(currBoard)
    currBoard = transposeBoard.transpose(currBoard)

    return currBoard

def returnMergeDown():
    updatedBoard = mergeDown(temporaryBoard.boardFill)
    temporaryBoard.display(updatedBoard)
