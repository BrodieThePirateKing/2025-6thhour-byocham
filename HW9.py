#Name: Brodie Yocham
#Class: 6th Hour
#Assignment: HW9

import random
#1. Print "Hello World!"
print("hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
my_list = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3. Print the list.
print(my_list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if  my_list[0] >= my_list[1] and my_list[0] >= my_list[2]:
    print("first is bigger than the second and third")
    num = my_list[0]
elif my_list[1] >= my_list[0] and my_list[1] >= my_list[2]:
    print("second is bigger than the first and third")
    num = my_list[1]
elif my_list[2] >= my_list[0] and my_list[2] >= my_list[1]:
    print("third is bigger than the first and second")
    num = my_list[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("is divisible by 2 and 3")
    else:
        print("is divisible by 2 but not 3")
else:
    if num % 3 == 0:
        print("is divisible by 3 but not 2")
    else:
        print("is divisible by neither")

