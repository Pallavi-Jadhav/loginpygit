from tkinter import *

mainwin= Tk()

username_label=Label(mainwin,text="Name")
password_label=Label(mainwin,text="Password")

user_entry=Entry(mainwin)
password_entry=Entry(mainwin)

username_label.grid(row=0,sticky=S)
password_label.grid(row=1, sticky=S)

user_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

c=Checkbutton(mainwin, text="Keep me logged in")
c.grid(columnspan=2)

mainwin.mainloop()