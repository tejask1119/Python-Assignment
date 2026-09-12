### Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount :

amount = int(input("Enter amount: "))

note_2000 = amount // 2000
amount = amount % 2000

note_500 = amount // 500
amount = amount % 500

note_200 = amount // 200
amount = amount % 200

note_100 = amount // 100
amount = amount % 100

note_50 = amount // 50
amount = amount % 50

note_20 = amount // 20
amount = amount % 20

note_10 = amount // 10
amount = amount % 10

total_notes = note_2000 + note_500 + note_200 + note_100 + note_50 + note_20 + note_10

print("2000 notes:", note_2000)
print("500 notes:", note_500)
print("200 notes:", note_200)
print("100 notes:", note_100)
print("50 notes:", note_50)
print("20 notes:", note_20)
print("10 notes:", note_10)
print("Minimum number of notes:", total_notes)