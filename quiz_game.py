print("Welcome to my computer quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's Play :) \n")
score = 1
answer = input("What does CPU stand for? ")

if answer.lower().strip() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
answer = input("What does GPU stands for? ")

if answer.lower().strip() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does RAM stands for? ")

if answer.lower().strip() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does ROM stand for? ")

if answer.lower().strip() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does PSU stands for? ")

if answer.lower().strip() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does HDD stands for? ")

if answer.lower().strip() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does SDD stand for? ")

if answer.lower().strip() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score/7) * 100}% ")
