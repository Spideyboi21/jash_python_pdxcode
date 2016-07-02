import random

def dice():
    return random.randint(1, 6)

player1 = 0
player2 = 0

while player1 < 20 and player2 < 20:
    pause = input("player1 press enter when ready to roll")
    player1 += dice()
    print("player1 you're score is now {}".format(player1))
    pause = input("player2 press enter when ready to roll")
    player2 += dice()
    print("player2 you're score is now {}".format(player2))
else:
    if player1 >= 20:
        print("player1 congrats you won!!!")
    else:
        print("player2 congrats you won!!!") 
