
import transposeBoard
import mergeLeft
import temporaryBoard

def mergeUp(currBoard):
    currBoard = transposeBoard.transpose(currBoard)
    currBoard = mergeLeft.mergeLeft(currBoard)
    currBoard = transposeBoard.transpose(currBoard)

    return currBoard

def returnMergeUp():
    updatedBoard = mergeUp(temporaryBoard.boardFill)
    temporaryBoard.display(updatedBoard)

    