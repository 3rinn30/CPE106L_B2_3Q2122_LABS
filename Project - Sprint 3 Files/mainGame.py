import temporaryBoard
import mergeLeft
import mergeRight
import mergeUp
import mergeDown
import copy

def initialBoard():
    temporaryBoard.display(temporaryBoard.boardFill)

def lost():
    board1 = copy.deepcopy(temporaryBoard.boardFill)
    board2 = copy.deepcopy(temporaryBoard.boardFill)

    board1 = mergeUp.mergeUp(board1)
    if board1 == board2:
        board1 = mergeDown.mergeDown(board1)
        if board1 == board2:
            board1 = mergeRight.mergeRight(board1)
            if board1 == board2:
                board1 = mergeLeft.mergeLeft(board1)
                if board1 == board2:
                    return True
    return False

def winner():
    for row in temporaryBoard.boardFill:
        if 2048 in row:
            return True
    return False

def callMove():
    move = input("Which direction do you want to merge?: ")
    validInput = True
    tempBoard = copy.deepcopy(temporaryBoard.boardFill)

    if move == "d":
        mergeDown.returnMergeDown()
    elif move == "l":
        mergeLeft.returnMergeLeft()
    elif move == "u":
        mergeUp.returnMergeUp()
    elif move == "r":
        mergeRight.returnMergeRight()
    else:
        validInput = False

    if not validInput:
        print("Invalid input, Please Try Again!")
    else:
        if temporaryBoard.boardFill == tempBoard:
            print ("No changes in the board, choose a different direction!")
        else:
            if winner():
                temporaryBoard.display(temporaryBoard.boardFill)
                print("Congratulations! You Won!")
                gameOver = True

            elif lost():
                print("Sorry, no moves are possible. Game Over!")
                gameOver = True
            else:
                temporaryBoard.AddValue()


def test():
    initialBoard()
    gameOver = False
    while not gameOver:
        callMove()


if __name__ == "__main__":
    test()