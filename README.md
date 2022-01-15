# Tkinter

Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit and is Python's de-facto standard GUI.

## Installation

Use the following step to install PIL.

```bash
Location_of_your_python_compiler>cd scripts
Location_of_your_python_compiler>scripts>pip install pillow
```

## Pre-requisite
You must have a basic knowledge of 
List 
range(), 
random module, 
Method declaration, and definition.
then you should have Symentix knowledge of tkinter, itertools, and PIL.

## Imported modules
```python
import itertools
import random
from tkinter import *
from PIL import ImageTk, Image
```

## Project Description:
First of all, I have drawn an applet type page and changed the background color with giving a title name to root. 
```python
background_color="#0D865D"
root= Tk()
root.geometry("800x620")
root.title("Dice Simulator Game")
```

>Setting a heading as " Dice Simulator Game "with changing the font color and background color as well as font type with giving some padding value:
```python
HeadingLabel = Label(root, text="Dice Roller Simulator Game",
   fg = "white",
     bg = "black",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack(pady=50)
```

>Statically storing the path of the initial image to the variable and resized & repositioned by using tkinter,Image,Label,Pack and PhotoImage concept.

```python
first_image_path="C:\College\Python Project\Images\dice\d0.png"
second_image_path="C:\College\Python Project\Images\dice\d0.png"

first_dice_image=ImageTk.PhotoImage(Image.open(first_image_path))
first_image_label=Label(root,image=first_dice_image,bg=background_color,height=100 ,width=100)
first_image_label.pack(pady=20)

second_dice_image=ImageTk.PhotoImage(Image.open(second_image_path))
second_image_label=Label(root,image=second_dice_image,bg=background_color,height=100,width=100)
second_image_label.pack(pady=20)
```




## rool_dice method
>This function is generating list of range 1 to 7 and chosing a random value two times and returning those two value to the calling method.
```python
def roll_dice():
    dice_number=list(range(1,7))
    combinations=list(itertools.product(dice_number,repeat=2))
    
    rolled_dice=random.choice(combinations)
    return rolled_dice
```

## update_roll_dice_image method
>Here we are calling the method rool_dice() and storing those list values into rolled_dice variable and printing them to the output terminal.
```python
 rolled_dice=list(roll_dice())
    print(rolled_dice)
```
>and then reading both values of the list and finding the path of the image related to that list value. Again we will be reading image paths, opening and labeling them, and will be updating the image, and configuring these.

## Roll Dice Button
>The button concept has been used and generated a button with changed font as well as the front color and repositioned with having padding value 20, bottom position and background color as blue.
```python
roll_button=Button(root,text="Roll Dices!",font = "Helvetica 16 bold italic",fg="blue",command=update_roll_dice_image)
roll_button.pack(side=BOTTOM,pady=30)
root.configure(bg=background_color) 
```

## Issue
>when I run the code everything works perfectly but the images are not changing on the front part.
.
When I analyzed the code, I felt that there may be an issue with lines number 47 &48. Please help me rectify this if there is any problem.

>Would be happy to get your helpful contribution.



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


