import temporaryBoard
import mergeLeft

def initialBoard():
    temporaryBoard.display(temporaryBoard.boardFill)

def callMove():
    move = input("Which direction do you want to merge?: ")
    validInput = True

    if move == "l":
        mergeLeft.returnMergeLeft()

def test():
    initialBoard()
    callMove()

if __name__ == "__main__":
    test()