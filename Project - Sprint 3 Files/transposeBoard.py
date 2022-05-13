
boardSize = 4

def transpose(currBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currBoard[j][i]
                currBoard[j][i] = currBoard[i][j]
                currBoard[i][j] = temp
    return currBoard