## 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

number_of_students = int(input("Enter number of students: "))

total_percentage = 0

for student in range(1, number_of_students + 1):

    total_marks = 0

    for subject in range(1, 6):
        marks = float(input("Enter marks of subject: "))
        total_marks = total_marks + marks

    percentage = total_marks / 5

    print("Student", student, "Percentage:", percentage)

    total_percentage = total_percentage + percentage

average_percentage = total_percentage / number_of_students

print("Average Percentage:", average_percentage)