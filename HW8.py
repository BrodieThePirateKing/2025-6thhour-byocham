#Name: Brodie Yocham
#Class: 5th Hour
#Assignment: HW8
import random
#1. Print "Hello World!"
print("hello world")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
A = random.randint(1, 10)
B = random.randint(1, 10)
C = random.randint(1, 10)
#3. Print A, B, and C on the same line.
print(A, B, C)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if A > 5:
    print(A, "is greater than 5")
elif B < 5:
    print(B, "is less than 5")
else:
    print(C, "is equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if C <= 3 and C <= 7:
    print(B, "is between 3 and 7")
else:
    print(C, "is not between 3 and 7")
#6. Make an if statement that prints if variable C is even or odd.
if B % 2 == 0:
    print(C, "is even")
else:
    print(B, "is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
op_var = 3 + random.randint(1, 20)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
added_var = A + B + C

if op_var > added_var:
    print(added_var, "is less than", op_var)
elif op_var < added_var:
    print(added_var, "is greater than", op_var)
else:
    print(added_var, "is equal to", op_var)