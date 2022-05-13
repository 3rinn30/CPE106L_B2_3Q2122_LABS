boardSize = 4

def inverse(row):
    inversed = []
    for i in range(boardSize - 1, -1, -1):
        inversed.append(row[i])
    return inversed