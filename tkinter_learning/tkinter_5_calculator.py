from tkinter import *

root = Tk()
root.title("Simple Calculator")
global action 
action = 0

def button_click(number):
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def do_thing():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0,END)    

def add_click():
    do_thing()
    global action    
    action = 1
    
    
def minus_click():
    do_thing()
    global action    
    action = 2

def multiply_click():
    do_thing()
    global action    
    action = 3

def divide_click():
    do_thing()
    global action    
    action = 4

def equal_click():
    second_num = e.get()
    global s_num
    global action

    s_num = int(second_num)

    e.delete(0,END)
    if action == 1:
        e.insert(0, str(f_num + s_num))
    elif action == 2:
        e.insert(0, str(f_num - s_num))
    elif action == 3:
        e.insert(0, str(f_num * s_num))
    elif action == 4:
        e.insert(0, str((f_num / s_num) ))
    


    

def clear_click():
    global action

    action = 0
    f_num = 0
    s_num = 0
    e.delete(0,END)



# Create Entry window
# width, bg, fg, borderwidth
e = Entry(root, width=35, borderwidth=5)



# Declare buttons
# Numerals
button_1 = Button(root, text='1', padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command= lambda: button_click(0))
# Actions
button_plus = Button(root, text='+', padx=39, pady=20, command=add_click)
button_minus = Button(root, text='-', padx=39, pady=20, command=minus_click)
button_multiply = Button(root, text='*', padx=39, pady=20, command=multiply_click)
button_divide = Button(root, text='/', padx=39, pady=20, command=divide_click)
button_equal = Button(root, text='=', padx=86, pady=20, command=equal_click)
button_clear = Button(root, text='C', padx=40, pady=10, command=clear_click)

# Project buttons in grid
# Row 0
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
button_clear.grid(row=0, column=3)
# Row 1
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

# Row 2
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

# Row 3
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

# Row 4
button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)
button_divide.grid(row=4, column=3)



# Make a loop to keep screen open
root.mainloop()
