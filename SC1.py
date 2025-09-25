#Name: Brodie
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1: print those changes
#to confirm they went through.
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their pr changes
#to the enemy's damage values for balancing, as well as having it

#It is up to you to decide what properties are important and the theme of the game.

#for combat testing. Additionally, the testers are asking for a way to input

Terraria_dict = {
    "Zombie" : {
        "Health" : 135,
        "Damage" : 42
    },
   "Eye of Cthulhu": {
        "Health" : 4641,
        "Damage" : 45
    },
    "Moon_Lord": {
        "Health" : 277311,
        "Damage" : 150
    },
    "Slime": {
        "Health": 75,
        "Damage": 21

    }, "Lunatic_Cultists": {
        "Health" : 400,
        "Damage" : 80
    },
}

variable_1 = input("Zombie, Eye of Cthulhu, Moon_Lord, Slime, Lunatic_Cultists" )
print(Terraria_dict[variable_1])
Terraria_dict[variable_1].update({"Damage" : int(input ("One Piece"))})
print(Terraria_dict[variable_1])
