import tkinter
import random

window = tkinter.Tk()


def RandomName():
    names = ["Haziq", "Ved", "Joshua", "Bryan"]
    MyRandom = random.choice(names)
    dice_thrown.configure(text="Name: " + str(MyRandom))


MyTitle = tkinter.Label(window, text="Random Name Generator", font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="Press me!!!!!!!!", command=RandomName)
MyButton.pack()

dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
dice_thrown.pack()

window.mainloop()
