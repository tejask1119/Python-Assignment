## Write a program to calculate the percentage of student based on marks of any 5 subjects.

python = int(input("enter Python marks.."))
java = int(input("enter Java marks.."))
c = int(input("enter c marks.."))
Os = int(input("enter Os marks.."))
Da = int(input("enter Da marks.."))

totalMarks = python + java + c + Os + Da 
print("Total marks : 500 /",totalMarks)

percentage = totalMarks / 5
print("percentage : 100% ",percentage)