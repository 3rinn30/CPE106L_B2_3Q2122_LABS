"""
Program: generator_modified.py
Author: John Raeniel Aberia & John Gabriel Javier
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

def getWords(filename):
    f = open(filename, 'r')
    temporaryList = list()

    for line in f:
        line = line.strip()
        temporaryList.append(line)

    all = tuple(temporaryList)
    f.close()
    return all

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()

