from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#Examples
class examples:
	def __init__(self):
		self.gap ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73124" # N
		self.MCBd ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=71093" # Y
		self.MCBa ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=67997" # N
		self.MCBc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73862" # Y
		self.MCc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73865"
		self.MCd =""

def init():
	e = examples()
	#userDesired = input("Desired User \n")
	#passDesired = input("Desired Password \n")
	#pageDesired = input("Desired Page Name \n")
	pageDesired = e.MCc
	userDesired = "17ABryan"
	passDesired = "SilkyCat01"
	
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

	
	if I != None:
		answers = I[0][1]
		answer = []
		for i in range(len(answers)):
			answer.append(answers[i][0])
		answers = answer

		i = 0
		options = []
		complete = False
		pass
		while complete == False:
			try:
				element = Select(driver.find_element_by_id("Gap0"))
				element.select_by_value("GapContentId_"+str(i))
				options.append(element.first_selected_option.text)
			except:
				complete = True
			i += 1
		if options == []:
			pass
			qType = "Gap"
		else:
			if arrEqual(answers,options) == True:
				qType = "MultiChoiceBox_C"
				pass
			else:
				qType = "MultiChoiceBox_A"
				pass

	try:
		driver.find_element_by_id("Questions")
		try:
			element = driver.find_element_by_id("ShowMethodButton")
			driver.click()
			qType = "MultiChoiceBox_D"
		except:
			pass
			qType = "MultiChoiceButton"
	except:
		pass	
	return [qType,driver.find_elements_by_id("GapSpan")]

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
		#Finds Multichoice boxes
		i = 0
		complete = False
		while complete == False:
			try:
				element = Select(driver.find_element_by_id("s"+str(i)+"_"+str(i)))
				elem.append(element)
				i += 1
			except:
				complete = True

		#Finds how many options each multichoice has
		options = []
		for j in range(len(elem)):
			options.append(None)
			complete = False
			i = 0
			while complete == False:
				try:
					element = Select(driver.find_element_by_id("s"+str(j)+"_"+str(j)))
					element.select_by_value(str(i))
					options[j] = i+1
					i +=1
				except:
					complete = True
				driver.get(pageDesired)

		#Solves Multichoice

		answers = []
		for j in range(max(options)+1):
			for i in range(len(elem)):
				try:
					element = Select(driver.find_element_by_id("s"+str(i)+"_"+str(i)))
					element.select_by_value(str(j))
				except:
					try:
						value = answers.index(i)
					except ValueError:
						answers.append(i)
			element = driver.find_element_by_id("CheckButton2")
			element.click()

		driver.get(pageDesired)

		for i in range(len(elem)):
			element = Select(driver.find_element_by_id("s"+str(i)+"_"+str(i)))
			element.select_by_value(str(answers[i]))
		driver.execute_script("CheckAnswers()")

	elif type == "C":
		i = 0
		complete = False
		while complete == False:
			try:
				element = Select(driver.find_element_by_id("Gap"+str(i)))
				elem.append(element)
				i += 1
			except:
				complete = True

		#Finds how many options each multichoice has
		options = []
		for j in range(len(elem)):
			options.append(None)
			complete = False
			i = 0
			while complete == False:
				try:
					element = Select(driver.find_element_by_id("Gap"+str(j)))
					element.select_by_value("GapContentId_"+str(i))
					options[j] = i+1
					i +=1
				except:
					complete = True
		driver.get(pageDesired)

		#Solves Multichoice

		answers = []
		for i in range(len(elem)):
			answers.append(None)
			for j in range(options[i]):
				answers[i] = "GapContentId_" + str(j)
				element = Select(driver.find_element_by_id("Gap" + str(i)))
				element.select_by_value(answers[i])
				driver.execute_script("CheckAnswers()")
				try:
					driver.find_element_by_id("Gap"+str(i))
				except:
					break
		driver.get(pageDesired)
		for i in range(len(elem)):
			element = Select(driver.find_element_by_id("Gap" + str(i)))
			element.select_by_value(answers[i])
		driver.execute_script("CheckAnswers()")
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
		for j in range(len(Answers[i])-1):
			if Answers[i][j][1] == 'Alles klar! Sehr gut! ':
				element = driver.find_element_by_id("Q_"+str(i)+"_"+str(j)+"_Btn")
				element.click()

def arrEqual(answers,options):
	for i in range(len(answers)):
		if answers[i]!=options[i]:
			return False
	return True

if __name__ == "__main__" :
	driver = webdriver.Chrome()
	pageDesired = init()
	Answers = []
	qNotType = []
	try:
		I = driver.execute_script("return I")
	except:
		I = None
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
	
