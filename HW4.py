#Name:Brodie Yocham
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
Straw_Hat_Pirates = ["Luffy", "Nami", "Franky", "Chopper", "Robin", "Sanji", "Zoro", "Brook"]
#2. Append a new name onto the Name List.
Straw_Hat_Pirates.append("Usopp")
#3. Print out the 4th name on the list.
print(Straw_Hat_Pirates[3])
#4. Create a list with 4 different integers in it.
jon_jon = [6, 7, 8, 9,]
#5. Insert a new integer into the 2nd spot and print the new list.
jon_jon.insert(1, 2)
print(jon_jon)
#6. Sort the list from lowest to highest and print the sorted list.
jon_jon.sort()
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(jon_jon[0] + jon_jon[1] + jon_jon[2])
#8. Create a list with two strings, two variables, and too boolean values.
my_list = (9, 0, False, True, "Ace", "Law")
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(Straw_Hat_Pirates[int(input())])