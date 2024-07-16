import random

randNum = random.randint(1, 100)

while True:
    userNum = int(input("Guess the number (1-100): "))
    if userNum == randNum:
        print("Congrats!!!You Guess The Right Number")
        break

    elif(userNum > randNum):
        print("Your number was too big , Guess smaller number") 

    else:
        print("Your number was too small , Guess bigger number")  

print("---GAME OVER---")
        

