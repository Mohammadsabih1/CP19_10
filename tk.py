import tkinter as tk

root = tk.TK()

v = tk.IntVar()
v.set(1)

languagues =[
	("Python",1),
	("Perl",2),
	("Java",3"),	
	("C",5)
]

def ShowChoice():
	print(v.get())

tk.Label(root,
	text="""Choose your favourite programming language:""",
		justify = tk.LEFT,
		padx = 20).pack()

for val, language in enumerate(language):
	tk.Radiobutton(root,
		text=language,
		padx =20,
		variable=v,
		command=ShowChoice,
		value=val).pack(anchor=tk.w)
root.mainloop()