import random

option = ('rock','paper','scissor')
player = None

computer = random.choice(option)

running = True
while running:
    while player  not in option:
        player = input("Enter your choice : (rock ,paper,scissor)")


    print(f'plsyer choice :{player}')
    print(f'computer choice : {computer}')

    if player == computer:
        print("there is tie")
    elif player =="rock" and computer =="scissor":
        print("You win")
    elif player =="paper" and computer =="rock":
        print("You win")
    elif player =="scissor" and computer =="paper":
        print("You win")
    else:
        print("You Lose")
    
    if not input("play again (y/n):").lower()=="y":
        running = False
print("thanks for playing")