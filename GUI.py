import tkinter as tk
from tkinter import messagebox
root=tk.Tk()


root.geometry("500x300")
root.title("Hangman Game")
def ab():
	messegebox.showinfo("Hello User",x1.get())
	x1.get("ok")
def cd():
	messegebox.showinfo("Hello User","hello world")
	x1.get("try again")

B1=tk.Button(root,text="Hello" ,command=ab)
B2=tk.Button(root,text="Hello User" ,command=cd)
B1.pack()
B2.pack()
root.mainloop()