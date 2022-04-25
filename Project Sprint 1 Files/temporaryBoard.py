# This python program will printout a temporary board for initial run and creation of the Project.

boardFill = [[2,2,0,4], [2,2,32,0], [0,0,0,0], [2,4,2,0]]

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