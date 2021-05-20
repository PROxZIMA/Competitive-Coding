class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        marks = sum(scores)/len(scores)
        if 90 <= marks <= 100:
            return 'O'
        elif 80 <= marks < 90:
            return 'E'
        elif 70 <= marks < 80:
            return 'A'
        elif 55 <= marks < 70:
            return 'P'
        elif 40 <= marks < 50:
            return 'D'
        else:
            return 'T'
    

firstName, lastName, idNum = input().split()
numScores = input()
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())