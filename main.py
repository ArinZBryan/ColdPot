from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#Examples
class examples:
	def __init__(self):
		self.gap ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73124"
		self.MCBd ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=71093"
		self.MCBa ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=67997"
		self.MCBc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73862"
		self.MCc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73865"
		self.MCd =""

def init():
	e = examples()
	#userDesired = input("Desired User \n")
	#passDesired = input("Desired Password \n")
	#pageDesired = input("Desired Page Name \n")
	userDesired = "17ABryan"
	passDesired = "SilkyCat01"
	pageDesired = e.MCBd
	
	driver.get("https://vle.rgshw.com/index.php")
	element = driver.find_element_by_id("username")
	element.send_keys(userDesired)
	element = driver.find_element_by_id("password")
	element.send_keys(passDesired, Keys.ENTER)
	driver.get("https://vle.rgshw.com/course/view.php?id=3004")
	driver.get(pageDesired)
	return pageDesired

def findQType():
	try:
		elem = driver.find_elements_by_id("GapSpan")			#Current MultiChoice Format
		qType = "MultiChoiceBox_C"
		I = driver.execute_script("return I")					#AnswersAvailable MultiChoice Format
		qType = "MultiChoiceBox_A"
	except:
		pass
	try:
		elem = driver.find_elements_by_class_name("GapBox")		#Try Gap Fill Solution
		qType = "Gap"
	except:
		pass
	try:
		element = driver.find_element_by_id("Questions")		#Depricated MultiChoice Format
		qType = "MultiChoiceBox_D"
	except:
		pass
	try:
		element =  driver.find_element_by_id("ShowMethodButton")#T/F MultiChoice Format
		qType = "MultiChoiceButton"
		element.click()
	except:
		pass
	return [qType,elem]

def gapFill():
	I = driver.execute_script("return I")
	Answers = []
	for i in range(len(I)):
		Answers.append(I[i][1][0][0])
	for j in range(len(elem)):								
		element = driver.find_element_by_id("Gap" + str(j))	
		element.send_keys(Answers[j])						
	driver.execute_script("CheckAnswers()")				
	print("Done!")

def MultiChoiceBox(type,pageDesired):
	if type == "D":
		sBoxes = []
		sBoxes.append(driver.find_elements_by_tag_name("select"))
		index = len(sBoxes)-1
		sBoxes[0].pop(index)
		Answers = []
		iteration = 0
		complete = False
		while complete == False:
			for i in range(len(sBoxes[0])-1):
				curBox = sBoxes[0][i]
				try:
					Select(curBox)
					curBox.select_by_index(iteration)
					Answers.append(iteration)
				except:
					complete = True
			iteration += 1
		driver.get(pageDesired)
		for i in range(len(sBoxes)-1):
			sBoxes[i].select_by_index(Answers[i])


	elif type == "C":
		pass
	elif type == "A":
		I = driver.execute_script("return I")
		for i in range(len(I)):
			sElement = Select(driver.find_element_by_id("Gap"+str(i)))
			sElement.select_by_visible_text(I[i][1][0][0])
		driver.execute_script("CheckAnswers()")

def MultiChoiceButton():
	I = driver.execute_script("return I")	
	for i in range(len(I)):
		Answers.append(I[i][3])
		print(Answers[i])
		for j in range(len(Answers[i])):
			if Answers[i][j][1] == 'Alles klar! Sehr gut! ':
				element = driver.find_element_by_id("Q_"+str(i)+"_"+str(j)+"_Btn")
				element.click()


if __name__ == "__main__" :
	driver = webdriver.Chrome()
	pageDesired = init()
	Answers = []
	qNotType = []
	fqt = findQType()
	qType = fqt[0]
	elem = fqt[1]

	if qType == "Gap":
		gapFill()
	elif qType == "MultiChoiceBox_D":
		MultiChoiceBox("D",pageDesired)
	elif qType == "MultiChoiceBox_C":
		MultiChoiceBox("C",pageDesired)
	elif qType == "MultiChoiceBox_A":
		MultiChoiceBox("A",pageDesired)
	elif qType == "MultiChoiceButton":
		MultiChoiceButton()
	print("e")
	