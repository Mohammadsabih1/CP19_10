
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
root=tk.Tk()


root.geometry("400x200")
root.title("tESTING")
def ab():
	messegebox.showinfo("Hello User",x1.get())
	x1.get("ok")
def cd():
	messegebox.showinfo("Hello User","hello world")

B1=tk.Button(root,text="Hello" ,command=ab)
B2=tk.Button(root,text="Hello User" ,command=cd)
B1.pack()
B2.pack()
root.mainloop()

