"""
Program: stats.py
Author: Erinn Chloe F. Sanchez
Computes for the median and mode of a set of numbers
"""

fileName = input("Enter the file name: ")
f = open(fileName, "r")

count = 0
for line in f:
    count = count + 1

print("The opened file has " +str(count)+ " lines")
f.close()

while True:
    try:
        n = int(input("Enter the line number you want to see [0 to quit]: "))
        number = 0
        break;
    except ValueError:
        print("Line number should be between 0 and "+str(count))
while n != 0:
    if n >= 0 and n <= count:
        f = open(fileName, "r")
        for line in f:
            number = number + 1
            if number == n:
                print(line)
        f.close()
    else:
        print("Line number should be between 0 and "+str(count))
    while True:
        try:
            n = int(input("Enter the line number you want to see [0 to quit]: "))
            number = 0
            break;
        except ValueError:
            print("Line number should be between 0 and "+str(count))