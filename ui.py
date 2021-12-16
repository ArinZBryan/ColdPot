import tkinter as tk

def start():
	userDesired = e1.get()
	passDesired = e2.get()
	subjectDesired = e3.get()
	questionDesired = e4.get()

master = tk.Tk()
tk.Label(master, text="VLE Username").grid(row=0)
tk.Label(master, text="VLE Password").grid(row=1)
tk.Label(master, text="Subject URL").grid(row=2)
tk.Label(master, text="Question URL").grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=0, pady=1)
tk.Button(master, text='Do It', command=start).grid(row=4, column=1, pady=1)

tk.mainloop()