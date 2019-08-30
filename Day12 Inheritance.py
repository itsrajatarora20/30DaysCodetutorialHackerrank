class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,fname,lname,idno,scr):
            super().__init__(fname,lname,idno)
            self.score=scr
    def calculate(self):
        iAvg = sum(self.score)/len(self.score)
        if iAvg >= 90 and iAvg<=100:
            return 'O'
        elif iAvg>=80 and iAvg<90:
            return 'E'
        elif iAvg>=70 and iAvg<80:
            return 'A'
        elif iAvg>=55 and iAvg<70:
            return 'P'
        elif iAvg>=40 and iAvg<55:
            return 'D'
        elif iAvg<40:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
