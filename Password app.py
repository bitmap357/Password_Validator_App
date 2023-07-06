from tkinter import *
import bcrypt


def validate(password):
    hashed = b'$2b$12$zHXl32aL20iFa6HYSubn4Ogvrjj6BYl1AX4nb7CnI63ieBaLe67Wm'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hashed):
        print("Log in successful")
    else:
        print("Invalid password")


root = Tk()
root.geometry('300x300')

password_entry = Entry(root)
password_entry.pack()

button = Button(root, text='Validate', command=lambda: validate(password_entry.get()))
button.pack()


root.mainloop()
