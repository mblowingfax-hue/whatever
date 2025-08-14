print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Way = input("Which way do you want to go, Left or Right?")
if Way == "left":
    print("You've come across a lake. There is an island in the middle of the lake")
else:
    print("You fell into a hole and fucking died. Game over")
    exit()
Action = input("Type 'wait' to wait for a boat. Type 'swim' to swim to the island. ")
if Action == "wait":
    print("The boat has arrived to the island.")
else:
    print("You dumbass were eaten by a fucking shark smh.")
    exit()
Decision = input("There are three doors in front of you. Red, Blue and yellow")
if Decision == "red":
    print("You encounter a black gang and get shot. Game over")
elif Decision == "blue":
    print("You come across an indian tribe and died from the smell. Game over.")
else:
    print("You found the treasure. Woohoooooooo!!!")
