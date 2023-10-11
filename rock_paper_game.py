import random
#rock paper scissor game
"""
two players one is system and one is user
game rules are user input is rock then computer input is paper
computer wins and so on like that
"""

#p>r,s>p,r>s
def is_win(user,comp):
    #return true if user wins, false if computer wins
    if (user== 'p' and comp=='r') or (user=='s' and comp=='p') \
        or (user=='r' and comp=='s'):
        return True
def play(n):
    gamelist=["r","p","s"]
    user_points,comp_points=0,0
    for i in range(n):
        user_choice=input("choose one r for rock,p for paper or s for scissor")
        comp_choice=random.choice(gamelist)
        print("user choice is",user_choice)
        print("comp_choice is",comp_choice)
        if user_choice==comp_choice:
            print("its a tie")
        elif is_win(user_choice,comp_choice):
            print("yahoo user wins")
            user_points+=1
        else:
            print("computer wins")
            comp_points+=1
    if user_points>comp_points:
        print("the game winner is user",user_points)
    elif user_points<comp_points:
        print("the computer won this time",comp_points)
    else:
        print("both players has same points")

play(5)
    




