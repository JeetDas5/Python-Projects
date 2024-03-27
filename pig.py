import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the numbers of the players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Input not in range. Try Again!")
            continue
    else:
        print("Input is not numeric. Try Again!")
        
# Initialize variables for player names and scores
player_names = ["Player " + str(i + 1) for i in range(players)]
scores = [0] * players
turns = 0

print("\nWelcome to Dice Pig!\n")
for name in player_names:
    print(name + ", you are up!")

while turns < 5: # Number of turns per game
    dice_roll = roll()
    print("You rolled a", dice_roll)
    
    selected_player = int(  input("Which player should get points? (1-{}) ".format(players)) ) - 1
    if selected_player >= players or selected_player < 0:
        print("Invalid player. Try Again!")
        continue
    
    scores[selected_player] += dice_roll
    print("Your score is now", scores[selected_player])
    
    turns += 1
    
    if turns == 5:  # Number of turns per game
        print("Game Over!")
        winner = max(scores)
        print("The winner is", player_names[scores.index(winner)])

    
