print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
print("Welcome to the treasure island!")
choice1=input("You are at a cross road to find a treasure now choose which way you would like to go either Left or Right?\n").lower()

if choice1=="left":
    choice2=input("You have arried at sea please select how would like to go to the Island>? Swim or Wait\n").lower()
    if choice2=="swim":
        print("You are attacked by a blue wale you are dead, Game Over!")
    if choice2== "wait":
        print("You have reached the Island, there is a house with three doors with Blue, Red, Yellow")
        choice3=input("please select which door you want to open to see the treasure? Blue, Red, Yellow:\n").lower()
        if choice3=="blue":
            print("Game over! You fell into a hole")
        elif choice3=="red":
            print("Game Over! You entered into a room full of fire.")
        elif choice3=="yellow":
            print("Hurray! you have found the treasure and you win!")
        else:
            print("Game Over! please choose the Right option and try again to find the treasure.")
else:
    print("You fell into the well, Game over you did not find the treasure")
