## Input 5 subject marks from user and display grade(eg.First class,Second class :

marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))
marks4 = float(input("Enter marks of subject 4: "))
marks5 = float(input("Enter marks of subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 35:
    print("Pass Class")
else:
    print("Fail")