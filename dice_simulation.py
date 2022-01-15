import itertools
import random
from tkinter import *
from PIL import ImageTk, Image

background_color="#0D865D"
root= Tk()
# image_path="C:\College\Python Project\Images\prateek.JPG"
# image=ImageTk.PhotoImage(Image.open(image_path))

# label_image=Label(root,image=image)
# label_image.pack(side=TOP)

root.geometry("800x620")
root.title("Dice Simulator Game")
HeadingLabel = Label(root, text="Dice Roller Simulator Game",
   fg = "white",
     bg = "black",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack(pady=50)

first_image_path="C:\College\Python Project\Images\dice\d0.png"
second_image_path="C:\College\Python Project\Images\dice\d0.png"

# first_image_path="C:\College\Python Project\Images\prateek.JPG"
# second_image_path="C:\College\Python Project\Images\prateek.JPG"

first_dice_image=ImageTk.PhotoImage(Image.open(first_image_path))
first_image_label=Label(root,image=first_dice_image,bg=background_color,height=100 ,width=100)
first_image_label.pack(pady=20)

second_dice_image=ImageTk.PhotoImage(Image.open(second_image_path))
second_image_label=Label(root,image=second_dice_image,bg=background_color,height=100,width=100)
second_image_label.pack(pady=20)

def roll_dice():
    dice_number=list(range(1,7))
    combinations=list(itertools.product(dice_number,repeat=2))
    
    rolled_dice=random.choice(combinations)
    return rolled_dice

def update_roll_dice_image():
    rolled_dice=list(roll_dice())
    print(rolled_dice)
    
    new_first_image_path="C:\College\Python Project\Images\dice\d{}.png".format(rolled_dice[0])
    new_second_image_path="C:\College\Python Project\Images\dice\d{}.png".format(rolled_dice[1])
    
    
    new_first_dice_image=ImageTk.PhotoImage(Image.open(new_first_image_path))
    new_second_dice_image=ImageTk.PhotoImage(Image.open(new_second_image_path))
    
    first_dice_label=Label(image=new_first_dice_image)
    second_dice_label=Label(image=new_second_dice_image)
    
    first_dice_label.configure()
    second_dice_label.configure()
    
    first_dice_label.image=new_first_dice_image
    second_dice_label.image=new_second_dice_image


roll_button=Button(root,text="Roll Dices!",font = "Helvetica 16 bold italic",fg="blue",command=update_roll_dice_image)
roll_button.pack(side=BOTTOM,pady=30)
root.configure(bg=background_color)

root.mainloop()