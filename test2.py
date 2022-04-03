import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class examples:
	def __init__(self):
		self.gap ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73124"
		self.MCBd ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=71093"
		self.MCBa ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=67997"
		self.MCBc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73862"
		self.MCc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73865"
		self.MCd =""


	
def ui():
	master = tk.Tk()
	tk.Label(master, text="VLE Username").grid(row=0)
	tk.Label(master, text="VLE Password").grid(row=1)
	tk.Label(master, text="Subject URL").grid(row=2)
	tk.Label(master, text="Question URL").grid(row=3)

	out = tk.StringVar(master)
	out.set("mcbD")
	options = ["Gap-Fill","Multiple Choice (Dropdown)","Multiple Choice (Buttons)"]

	e1 = tk.Entry(master)
	e2 = tk.Entry(master)
	e3 = tk.Entry(master)
	e4 = tk.Entry(master)
	e5 = tk.OptionMenu(master,out,*options)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e5.grid(row=5, column=2)

	tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=0, pady=1)
	tk.Button(master, text='Do It', command=start(e1,e2,e3,e4,out)).grid(row=5, column=1, pady=1)

	tk.mainloop()

def main(driver,typeDesired):
	if typeDesired == "MCB":
		try:
			elem = driver.find_elements_by_id("GapSpan")			#Current MultiChoice Format
			qType = "MultiChoiceBox_C"
			I = driver.execute_script("return I")					#AnswersAvailable MultiChoice Format
			qType = "MultiChoiceBox_A"
		except:
			pass
		try:
			element = driver.find_element_by_id("Questions")		#Depricated MultiChoice Format
			qType = "MultiChoiceBox_D"
		except:
			pass
	elif typeDesired == "MC":
		try:
			element =  driver.find_element_by_id("ShowMethodButton")#T/F MultiChoice Format
			qType = "MultiChoiceButton"
			element.click()
		except:
			pass
	elif typeDesired == "GAP":
		try:
			elem = driver.find_elements_by_class_name("GapBox")		#Try Gap Fill Solution
			qType = "Gap"
		except:
			pass
	else:
		tk.destroy()
	print(qType)

	
	
def init(userDesired,passDesired,subjectDesired,questionDesired,driver):
	driver.get("https://vle.rgshw.com/index.php")
	element = driver.find_element_by_id("username")
	element.send_keys(userDesired)
	element = driver.find_element_by_id("password")
	element.send_keys(passDesired, Keys.ENTER)
	driver.get(subjectDesired)
	driver.get(questionDesired)
	return questionDesired

def start(e1,e2,e3,e4,out):
	userDesired = e1.get()
	passDesired = e2.get()
	subjectDesired = e3.get()
	questionDesired = e4.get()
	typeDesired = out.get()
	if typeDesired == "Gap-Fill":
		typeDesired = "GAP"
	elif typeDesired == "Multiple Choice (Dropdown)":
		typeDesired = "MCB"
	elif typeDesired == "Multiple Choice (Buttons)":
		typeDesired = "MC"
	pageDesired = init(userDesired,passDesired,subjectDesired,questionDesired,webdriver.Chrome())
	main(webdriver.Chrome(),typeDesired)

ui()