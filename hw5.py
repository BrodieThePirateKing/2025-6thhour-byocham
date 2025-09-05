#Name: Brodie Yocham
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
brodie_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#2. Sort the list from highest to lowest.
brodie_list.sort(reverse=True)
#3. Create an empty list.
the_list = []
#4. Remove the median number from the first list and add it to the second list.
anything = brodie_list[4]
brodie_list.pop(4)
the_list.append(anything)
#5. Remove the first number from the first list and add it to the second list.
somethingelse = brodie_list[0]
brodie_list.pop(0)
the_list.append(somethingelse)
#6. Print both lists.
print(brodie_list)
print(the_list)
#7. Add the two numbers in the second list together and print the result.
variable = the_list[0] + the_list[1]
print(variable)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
brodie_list.append(variable)
the_list.pop(0)
the_list.pop(0)
#9. Sort the first list from lowest to highest and print it.
brodie_list.sort()
print(brodie_list)