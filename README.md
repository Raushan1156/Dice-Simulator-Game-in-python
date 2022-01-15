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



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

