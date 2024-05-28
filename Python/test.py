from tkinter import *

win=Tk()
win.geometry("700x350")

days= [ "sun" , "mon" ,"tue" ]

text=Text(win,width=80 ,height = 15)
text.pack()

for day in days :
    text.insert(END, day)


win.mainloop()
