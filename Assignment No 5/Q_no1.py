## 1. Write a program to prompt user to enter userid and password. If Id and :
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


correct_userid = "admin"
correct_password = "1234"

attempt = 1

while attempt <= 3:

    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful")
        break

    else:
        print("Invalid User ID or Password")
        attempt = attempt + 1

if attempt > 3:
    print("Maximum attempts reached. Program terminated.")