class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.scores = scores
    
    def calculate(self):
        avgScore = sum(self.scores)/len(self.scores)
        if avgScore >= 90 and avgScore <= 100:
            return 'O'
        elif avgScore >= 80 and avgScore < 90:
            return 'E'
        elif avgScore >= 70 and avgScore < 80:
            return 'A'
        elif avgScore >= 55 and avgScore < 70:
            return 'P'
        elif avgScore >= 40 and avgScore < 55:
            return 'D'
        else:
            return 'T'

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
