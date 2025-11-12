#Name: Brodie Yocham
#Class: 6th Hour
#Assignment: HW14
from enum import nonmember

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(6):
    print(i)
else:
    print("hello world")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for l in range(30):
    if l % 2 == 0:
        print(l)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for p in range(30):
    if p % 3 == 1:
        print(p)
#4. Create a for loop that prints 5 different animals from a list.
animals = ["zebra", "cat", "mouse", "horse", "monkey"]
for q in animals:
    print(q)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
my_string = "hello world"
reversed_string = my_string[::-1]
print(my_string)
print(reversed_string)
#6. Create a list containing 10 integers of your choice and print the list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
#7. Create two empty variables named evenNumbers and oddNumbers.
var_evenNumbers = []
print(var_evenNumbers)
var_oddNumbers = []
print(var_oddNumbers)
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = 0
odd_numbers = 0
for num in number:
    if num % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
print(f"number of even numbers: {even_numbers}")
print(f"number of odd numbers: {odd_numbers}")
#9. Create a variable that asks the user for an integer and an empty integer variable.
ask_var = None
while ask_var is None:
    try: ask_var = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input, please try again")
empty_var = None
print(f"the integer you typed is: {ask_var}")
print(f"the empty integer variable is: {empty_var}")
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
try:
    number = int(input("Enter a positive integer: "))
except ValueError:
    print("Invalid input, please try again")
else:
    if number < 0:
        print("factorial is not for negative numbers")
    elif number == 0:
        print("factorial of 0 is 1")
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(f"factorial of {number} is {factorial}.")