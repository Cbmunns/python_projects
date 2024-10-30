from tkinter import *

root = Tk()

def my_click():
    my_label = Label(root, text="You clicked the button!")
    my_label.pack()

# Create button and text inside button
# padxy will help dictate the size of the button
# Command calls a function after clicking button
# fg = foreground bg = background
my_button = Button(root, text="Click Me!", padx=50, pady=50, command=my_click)
# State will decide if the button is greyed out
# my_button = Button(root, text="Click Me!", state=DISABLED)


# Project button
my_button.pack()

# Make a loop to keep screen open
root.mainloop()
