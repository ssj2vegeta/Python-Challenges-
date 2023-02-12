import tkinter

window = tkinter.Tk()
window.wm_title("Pounds(lbs) to Kilograms(Kg)")
Base_Number = ""


def evaluate(event):
    if Base_Number == "Pounds":
        try:
            lbs = int(Myentry.get(), 2)
            kgg = (lbs/2.2)
            result1.configure(text="Kilogram is: " + str(kgg))
        except ValueError:
            result1.configure(text="Please enter valid number")
            result2.configure(text="")

    elif Base_Number == "Kilograms":
        try:
            kg = int(Myentry.get(), 2)
            lbss = (kg*2.2)
            result1.configure(text="Pound is: " + str(lbss))
        except ValueError:
            result1.configure(text="Please enter valid number")
            result2.configure(text="")
    else:
        result1.configure(text="Please select a unit!")


def calcStyle():
    global Base_Number
    Base_Number = base.get()
    print(base.get())


MyTitle = tkinter.Label(window, text="Weight Conversion")
MyTitle.pack()

Myentry = tkinter.Entry(window)
Myentry.bind("<Return>", evaluate)
Myentry.pack()

result1 = tkinter.Label(window, text="1. Choose a base")
result1.pack()

result2 = tkinter.Label(window, text="2. Enter a number and press<enter>")
result2.pack()

base = tkinter.StringVar()
tkinter.Radiobutton(window, text="Pound", variable=base, value="Pound", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Kilogram", variable=base, value="Kilogram", command=calcStyle).pack()

window.mainloop()
