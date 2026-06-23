import numpy as np
computer_score=0
player_score=0
def stone_paper():
    player=input("choose stone,paper or scissor ")
    l=['stone','paper','scissor']
    global player_score, computer_score

    comp=np.random.choice(l)
    if (player=="stone" and comp=="stone"):
        print("draw")
    elif(player=="stone" and comp=="paper"):
        print('computer wins')
        computer_score+=1
    elif(player=="stone" and comp=="scissor"):
        print('player wins')
        player_score+=1
    elif(player=="paper" and comp=="stone"):
        print('player wins')
        player_score+=1
    elif(player=="paper" and comp=="paper"):
        print("draw")
    elif(player=="paper" and comp=="scissor"):
        print('computer wins')
        computer_score+=1
    elif(player=="scissor" and comp=="stone"):
        print('computer wins')
        computer_score+=1
    elif(player=="scissor" and comp=='paper'):
        print('player wins')
        player_score+=1
    elif(player=="scissor" and comp=='scissor'):
        print("draw")

    print('computer score:',computer_score)
    print('player score:',player_score)
    if(player_score>computer_score):
        print("player wins")
    else:
        print("compter wins")

rounds=int(input("enter no of rounds"))
for i in range (rounds):
    stone_paper()