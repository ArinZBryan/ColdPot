import tkinter as tk

def start():
	userDesired = e1.get()
	passDesired = e2.get()
	subjectDesired = e3.get()
	questionDesired = e4.get()
	qTypeDesired = e5.get()

master = tk.Tk()
tk.Label(master, text="VLE Username").grid(row=0)
tk.Label(master, text="VLE Password").grid(row=1)
tk.Label(master, text="Subject URL").grid(row=2)
tk.Label(master, text="Question URL").grid(row=3)
tk.Label(master, text="Question Type").grid(row=4)

menuOptions = ["Gap fill", "Button-based selection", "Drop-down multichoice"]
clicked = tk.StringVar()
clicked.set("None Selected")


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.OptionMenu(master,clicked,*menuOptions)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=0, pady=1)
tk.Button(master, text='Do It', command=start).grid(row=5, column=1, pady=1)

dropDown = tk.OptionMenu(master, clicked,*menuOptions)
dropDown.pack


tk.mainloop()