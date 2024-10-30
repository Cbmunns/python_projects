from tkinter import*
from tkinter import font
from tkinter.ttk import*

from time import strftime

root = Tk()

root.title('Clock')

def time():
    string = strftime('      %a\n%I:%M:%S %p\n %m/%d/%Y')
    lbl.config(text=string)
    # lbl2.config(text=string)
    lbl.after(1000, time)
    # lbl2.after(1000, time)
    

lbl = Label(root, font=('comfortaa', 40, 'bold'),
            background='purple',
            foreground='white')

# lbl2 = Label(root, font=('comfortaa', 50, 'bold'),
#             background='purple',
#             foreground='black')


# lbl2.grid(row=0, column=1)
lbl.grid(row=0, column=0)
time()

mainloop()