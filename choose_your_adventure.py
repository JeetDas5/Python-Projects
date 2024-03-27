name = input("Type your name: ")
print(f"Welcome {name} to the adventure!!!")

answer = input("You are one a dirt road, you can go left or right. Which way would you like to go? ").lower()

if(answer == "left"):
    answer = input("You come to a river, you can walk around or swim across. Which way would you like to go? ").lower()
    
    if answer == 'swim':
        print("You swam across and were eaten by an alligator")
    if answer == 'walk':
        print("You walked for many miles, ran out of water and died of thirst")
    else:
        print("You got lost")
    
elif(answer == "right"):
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back) ").lower()
    if answer == 'back':
        print("You go back and lose")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? ").lower()
        if answer == 'yes':
            print("You made a new friend and he gave you a gold coin")
        elif answer == 'no':
            print("You are expelled from the brige")
        else:
            print("Not a valid option.You got lost")
    
else:
    print("You got lost")
    
print("Thank you for playing " + name)