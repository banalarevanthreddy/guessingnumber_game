import random
def game(low):
    rand_num= random.randint(1,low)
    r=5
    for i in range(1,r):
        guess=int(input("guess the number"))
        if guess==rand_num:
            print("yahoooo the guess is correct")
            break
        elif(guess<rand_num):
            print("the number is too low")
        else:
            print("the number is too high")
        print("you have only {} chances left!".format(r-i))
#game(10)

def computer_guess(y):
    my_input= int(input(f"enter the number between 1 and {y}"))
    low=1
    feedback=''
    while feedback!= 'c':
        comp_guess=random.randint(low,y)
        feedback= input(f"is {comp_guess} too high(h),too low(l), correct(c)").lower()
        print("computer guess is",comp_guess)
        if(feedback== 'h'):
            y= (comp_guess-1)
            print("-----------------")
            print(f"now the computer guesses between {low} and {y}")
        elif(feedback== 'l') :
            low=(comp_guess+1)
            print("-----------------")
            print(f"now the computer guesses between {low} and {y}")
    print("Computer wins")
computer_guess(50)


