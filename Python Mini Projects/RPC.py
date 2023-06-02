import random

comp=random.choice(('rock','paper','scissors'))
print(comp)

your_choice=input("Enter your choice out of (rock,paper,scissors): ")

if comp==your_choice:
    print("Tie,","Your Choice:",your_choice,"\tComputer's Choice:",comp)
else:
    if your_choice=='rock':
        if comp =='paper':
            print("You Lose.\t Your Choice: ",your_choice,"\tComputer's Choice: ",comp)
        else:
            print("You Win.\t Your Choice: ",your_choice,"\tComputer's Choice: ",comp)
    if your_choice=='paper':
        if comp =='rock':
            print("You Win.\t Your Choice: ",your_choice,"\tComputer's Choice: ",comp)
        else:
            print("You Lose.\t Your Choice: ",your_choice,"\tComputer's Choice: ",comp)
    if your_choice=='scissors':
        if comp =='rock':
            print("You Lose.\t Your Choice: ",your_choice,"\tComputer's Choice: ",comp)
        else:
            print("You Win.\t Your Choice: ",your_choice,"\tComputer's Choice: ",comp)

