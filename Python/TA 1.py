from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator  
from tkinter import messagebox

root = tk.Tk()
root.title('Langauge Translator')
root.geometry('750x330')
root.maxsize(1920,1024)
root.minsize(750,330)
root.configure(background='black')



def translate():
        language_1 = t1.get("1.0","end-1c")
        cl = choose_langauge.get()

        if language_1 == '':
                messagebox.showerror('Language Translator','please fill the box')
        else:
                t2.delete(1.0,'end')
                translator = Translator()
                output = translator.translate(language_1, dest=cl)
                t2.insert('end',output.text)

def clear():
        t1.delete(1.0,'end')
        t2.delete(1.0,'end')



a = tk.StringVar() 
any_language = ttk.Combobox(root, width = 33, textvariable = a, state='readonly',font=('verdana',10,'bold'),) 
  


any_language['values'] = ('Any Language',) 
  
any_language.place(x=30,y=70)
any_language.current(0) 





l = tk.StringVar() 
choose_langauge = ttk.Combobox(root, width = 33, textvariable = l, state='readonly',font=('verdana',10,'bold')) 
  


choose_langauge['values'] = ('English','French','German','Hindi','Marathi') 
  
choose_langauge.place(x=400,y=70)
choose_langauge.current(0) 


t1 = Text(root,width=39,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=30,y=100)

t2 = Text(root,width=39,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=400,y=100)


button = Button(root,text="Translate",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=translate)
button.place(x=150,y=280)


clear = Button(root,text="Clear",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=clear)
clear.place(x=540,y=280)

root.mainloop()
