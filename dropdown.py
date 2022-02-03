# Import module
from tkinter import *

def main(e1,e2,e3,e4,clicked):
	userDesiered = e1.get()
	passDesired =  e2.get()
	pageDesired e3.get(), e4.get(), clicked.get())

def ui():
	# Create object
	root = Tk()

	# Adjust size
	root.geometry( "200x200" )

	Label(root, text="VLE Username").grid(row=0)
	Label(root, text="VLE Password").grid(row=1)
	Label(root, text="Subject URL").grid(row=2)
	Label(root, text="Question URL").grid(row=3)

	e1 = Entry(root)
	e2 = Entry(root)
	e3 = Entry(root)
	e4 = Entry(root)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)

	# Dropdown menu options
	options = [
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday",
		"Sunday"
	]

	# datatype of menu text
	clicked = StringVar()

	# initial menu text
	clicked.set( "Monday" )

	# Create Dropdown menu
	drop = OptionMenu( root , clicked , *options )

	drop.grid(row = 5, column = 1)

	# Create button, it will change label text
	Button(root, text='Quit', command=root.quit).grid(row=4, column=0, pady=1)
	Button(root, text='Do It', command=main(e1,e2,e3,e4,clicked)).grid(row=4, column=1, pady=1)
	# Create Label
	label = Label( root , text = " " )


	# Execute tkinter
	root.mainloop()


if __name__ == "__main__":
	ui()
