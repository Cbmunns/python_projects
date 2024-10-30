from tkinter import *

root = Tk()
# Create label aka text
my_label1 = Label(root, text='Hello World!')
my_label2 = Label(root, text='My Name Is Chris Munns')
# Assigning specific locations on the grid
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0)

# Make a loop to keep screen open
root.mainloop()
