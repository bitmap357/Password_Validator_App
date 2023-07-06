from tkinter import *
import bcrypt

root = Tk()
root.geometry('300x300')

password_entry = Entry(root)
password_entry.pack()

button = Button(root, text='Validate', command=validate)
button.pack()


root.mainloop()
