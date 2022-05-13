import mergeLeft
import inverseRow
import temporaryBoard

def mergeRight(currBoard):
    for i in range(mergeLeft.boardsize):
        currBoard[i] = inverseRow.inverse(currBoard[i])
        currBoard[i] = mergeLeft.mergeoneRowL(currBoard[i])
        currBoard[i] = inverseRow.inverse(currBoard[i])
    return currBoard

def returnMergeRight():
    updatedBoard = mergeRight(temporaryBoard.boardFill)
    temporaryBoard.display(updatedBoard)