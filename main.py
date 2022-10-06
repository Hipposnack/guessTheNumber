from tkinter import *
import random

def guess():
    try:
        maximum = num1.get()
        max_final = int(maximum)
        src = sum.get()
        src_final = int(src)

        num = random.randint(0,max_final)

        if src_final > max_final:
            result.config(text=f"The number can't be bigger than {max_final}", fg="red")
            cor.config(text="")
            root.update()
        else:
            if src_final == num:
                result.config(text="Correct!",fg="green")
                cor.config(text=num)
                root.update()
            else:
                result.config(text="Wrong! The correct Number was:",fg="red")
                cor.config(text=num)
    except ValueError:
        result.config(text="Please enter a number", fg="red")
        root.update()


root = Tk()
root.geometry("420x420")
root.title("Guess the number")
title = Label(root,text="Guess the number!", font="Helvetica,100",fg="blue")
title.pack()
info = Label(root,font="arial,70",text="Maximum random number:",fg="black")
info.pack()
num1 = Entry(root)
num1.pack()
info2 = Label(root,font="arial,70",text="Guess the number:",fg="black")
info2.pack()
sum = Entry(root)
sum.pack()
sub = Button(root,text="Submit!",command=guess)
sub.pack()
result = Label(root,font="arial,70",text="",fg="green")
result.pack()
cor = Label(root,font="arial,70",text="",fg="black")
cor.pack()
root.mainloop()