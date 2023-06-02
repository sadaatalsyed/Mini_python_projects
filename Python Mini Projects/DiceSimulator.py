import random
from tkinter import *

#initializing window screen for display
windw=Tk()
#background color configuration
windw.configure(bg="black")
#setting hight and width
windw.geometry("1050x650")
#settin title for the game window
windw.title("Dice Rolling Game")
#setting resizeability if you want it flexible leave it blank
windw.resizable(2,2)
count=0
prev_face1=[]
prev_face2=[]
def dice_roll():
    global count
    count+=1
    global prev_face2
    global prev_face1
   
    dice_dots=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    dice1_face=random.choice(dice_dots)
    dice2_face=random.choice(dice_dots)
    label.configure(text=f' You have rolled the dice {count}  times.')
    curr_face1=dice_dots.index(dice1_face)+1
    curr_face2=dice_dots.index(dice2_face)+1
    if count>1:
        total.configure(text=f'Sum of current Faces: {curr_face1+curr_face2}\n Previous Scores for Dice1={prev_face1} \n Previous Scores for Dice2={prev_face2}')
    else:
        total.configure(text=f'Sum of current Faces: {curr_face1+curr_face2}')
    prev_face1.append(curr_face1)
    prev_face2.append(curr_face2)
    label.place(x=50,y=200)
    label.pack()
    total.pack(padx=10,pady=10)
    roll_label.configure(text=f'{dice1_face}{dice2_face}')
    roll_label.pack()
def Exit():
    windw.destroy()
    


# adding button to roll the dice
roll_button=Button(windw, text="Roll Dice", bg="green",width=10,height=2,bd=2, font=25,fg='yellow', command=dice_roll).pack()
roll_button=Button(windw, text="Exit", bg="red",width=10,height=2,bd=2, font=25,fg='yellow', command=Exit).pack()
roll_label = Label(windw, font=("times", 250),bg="black", fg="yellow")
label = Label(windw,  font=("times", 20),bg="black", fg="white")
total = Label(windw,  font=("times", 20),bg="black", fg="white")


#starting running the display
windw.mainloop()