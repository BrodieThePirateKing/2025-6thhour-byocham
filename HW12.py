#Name:Brodie Yocham
#Class: 5th Hour
#Assignment: HW12
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
else:
    print("Hello World")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
l = 2
while l <= 30:
    if l % 2 == 0:
        print(l)
    l += 2
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
l2 = 1
while l2 <= 30:
    if l2 % 3 == 1:
        l2 += 1
        continue
    print(l2)
    l2+=1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
while True:
    roll = random.randint(1,6)
    print(f"rolled a: {roll}")
    if roll == 1:
        print("rolled a 1, breaking the loop")
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
l3 = 10
while l3 >= 1:
    if l3 % 2 == 0:l3 = int(input("Enter a number: "))
    if l3 > 0:
        print(l3)
        continue
    else:
        print("thank you")