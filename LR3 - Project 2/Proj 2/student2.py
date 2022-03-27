"""
File: student2.py
Resources to manage a student's name and test scores. This also allows the students to be shuffled
and sort after, based on their scores and names.
"""
import random
class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def __init__(selfb, name, number):
        """All scores are initially 0."""
        selfb.name = name
        selfb.scores = []
        for count in range(number):
            selfb.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def setScore1(selfb, i, score):
        """Resets the ith score, counting from 1."""
        selfb.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def greaterThan(self, selfb):
        return self.scores > selfb.scores 

    def equal(self, selfb):
        return self.scores == selfb.scores 

    def lessThan(self, selfb):
        return self.scores < selfb.scores 



def main():
    """A simple test."""
    listStudents = []

    a = Student("Ken", 5)
    for i in range(1, 6):
        a.setScore(i, 75)
    listStudents.append(a)

    b = Student("Brian", 5)
    for i in range(1, 6):
        b.setScore1(i, 97)
    listStudents.append(b)

    c = Student("Micki", 5)
    for i in range(1, 6):
        c.setScore(i, 66)
    listStudents.append(c)

    d = Student("Larter", 5)
    for i in range(1, 6):
        d.setScore1(i, 100)
    listStudents.append(d)

    random.shuffle(listStudents)

    print("Student List (Shuffled): ")
    for i in listStudents:
        print(i.__str__())

    listStudents.sort(key=lambda x: x.scores)

    print("\nStudents sorted by score: ")
    for i in listStudents:
        print(i.__str__())

    listStudents.sort(key=lambda x: x.name)

    print("\nStudents sorted by name: ")
    for i in listStudents:
        print(i.__str__())
    
    """Used in Project 1"""
    """print(f"{a.name} scores is equal to {b.name}: {a.equal(b)}")
    print(f"{a.name} scores is less than to {b.name}: {a.lessThan(b)}")
    print(f"{a.name} scores is greater than to {b.name}: {a.greaterThan(b)}")"""


if __name__ == "__main__":
    main()


