"""
Program: stats.py
Author: John Paulo D. Miranda
Computes for the median and mode of a set of numbers
"""

def main():
    """The main function for this script"""

    fileName = input("Enter the file name: ")
    g = open(fileName, 'r')
    med = median(g)
    print (med)

    h = open(fileName, 'r')
    mean1 = mean(h)
    print (float(mean1))

    i = open(fileName, 'r')
    mod = mode(i)
    print (mod)

def median(modd):
    numbers = []
    for number in modd:
        numbers.append(int(number))

    numbers.sort()
    midpoint = len(numbers) // 2
    print("The median is", end=" ")
    if len(numbers) % 2 == 1:
        modd = (numbers[midpoint])
        return modd
    else:
        modd = ((numbers[midpoint] + numbers[midpoint - 1]) / 2)
        return modd

def mean(f):

    numbers1 = []
    for number1 in f:
        numbers1.append(int(number1))

    numbers1.sort()
    length = len(numbers1)

    total = 0
    for x in numbers1:
        total += x
    
    mean = total/length
    
    print("The mean is", end=" ")
    return mean

def mode(m):
    nums = []
    for line in m:
        numsInLine = line.split()
        for num in numsInLine:
            nums.append(num.upper())

    theNumber = {}
    for num in nums:
        number = theNumber.get(num, None)
        if number == None:
            theNumber[num] = 1
        else:
            theNumber[num] = number + 1

    theMaximum = max(theNumber.values())
    for key in theNumber:
        if theNumber[key] == theMaximum:
            mode1 = key
            break
    print("The mode is", end=" ")
    return mode1


if __name__ == "__main__":
    main()
