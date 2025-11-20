#Name: Brodie Yocham
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
total_rate = 0
player_count = int(input("How many players? "))
print(player_count)
for i in range(1, player_count + 1):

    player_rate = int(input(f"player {i}, enter rating (1-5): "))
    while player_rate < 1 or player_rate > 5:
        player_rate =  int(input(f"player {i}, enter rating (1-5): "))
    else:
        total_rate += player_rate


print(total_rate / player_count)