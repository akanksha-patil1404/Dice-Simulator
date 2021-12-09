from tkinter import *
import random

dice=Tk()

dice.title("Dice simulator")

dice.geometry("600x500")

label=Label(dice ,font=("Helvitica",300), text="\u2680")
label.pack()


def rolldice():
    dice_list=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    label.configure(text = f'{random.choice(dice_list)}')
    label.pack()

button=Button(dice,font=("Helvitica",25,'bold'), text="Roll", command = rolldice)
button.pack()

dice.mainloop()
