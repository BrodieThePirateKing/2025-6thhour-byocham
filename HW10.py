#Name: Brodie Yocham
#Class: 6th Hour
#Assignment: HW10

#1. Print Hello World!
("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
sum_ting = 1
if wifi == True:
    if login == True:
        if admin == True:
            print("welcome")
            sum_ting += 1
        else:
            print("login failed, die")
    else:
        print("login failed, die")
else:
    print("login failed, die")
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".