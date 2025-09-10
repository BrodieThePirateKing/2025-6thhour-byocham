#Name: Brodie Yocham
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
dice1 = random.randint(1, 10)
dice2 = random.randint(1, 10)
dice3 = random.randint(1, 10)
#4. Print the three variables from #3 on the same line.
print(dice1, dice2, dice3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
dice = dice1 + 2
new = dice2  - 4
vari = dice3 * 1.5
#6. Print each result from #5 on the same line.
print(dice, new, vari)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
list_1 = [random.randint(1, 6),  random.randint(1, 6),  random.randint(1, 6), random.randint(1, 6)]
#8. Sort the list in #7 and print it.
list_1.sort()
print(list_1)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(list_1[1] + list_1[2], list_1[3])
#10. Create a list with 5 names of other students in this class and print the list.
new_list = ["Shane", "Greg", "Alaya", "Devon", "Connor"]
print(new_list)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(new_list)
print(new_list)
#12. Print a random choice from the list of names from #10.
print(random.choice(new_list))