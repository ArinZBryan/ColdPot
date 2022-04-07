from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from argparse import ArgumentParser
from argparse import HelpFormatter

#Examples
class examples:
	def __init__(self):
		self.gap ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73124" # N
		self.MCBd ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=71093" # Y
		self.MCBa ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=67997" # N
		self.MCBc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73862" # Y
		self.MCc ="https://vle.rgshw.com/mod/hotpot/attempt.php?id=73865"
		self.MCd =""

class SmartFormatter(HelpFormatter):
	def _split_lines(self, text, width):
		if text.startswith("R|"):
			return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
		return HelpFormatter._split_lines(self, text, width)

def init(*args):
	if len(args) != 0:
		if len(args) != 3:
			raise Exception("Incorrect number of arguments provided to init function")
		else:
			pageDesired = args[0]
			userDesired = args[1]
			passDesired = args[2]
	else:
		e = examples()
		pageDesired = e.MCBc
	
	#userDesired = input("Desired User \n")
	#passDesired = input("Desired Password \n")
	#pageDesired = input("Desired Page Name \n")
	
	
	driver.get(pageDesired)
	element = driver.find_element_by_id("username")
	element.send_keys(userDesired)
	element = driver.find_element_by_id("password")
	element.send_keys(passDesired, Keys.ENTER)
	
	return pageDesired

def findQType(basis):

	if basis == "t":
		try:
			element = driver.find_element_by_id("ShowMethodButton")
			element.click()
			qType = "MultiChoiceButton"
		except Exception as e:
			print(e)
			raise Exception("Wrong activity type")
	elif basis == "g":
		try:
			element = driver.find_elements_by_class_name("GapBox")
			qType = "Gap"
		except Exception as e:
			print(e)
			raise Exception("Wrong activity type")
	elif basis == "d":
		try:
			element = driver.find_elements_by_id("GapSpan")			#Current MultiChoice Format
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
	else:
		raise Exception("No activity type specified, how the fuck did you get here?")
	
	return [qType,element]

def gapFill():
	I = driver.execute_script("return I")
	Answers = []
	for i in range(len(I)):
		Answers.append(I[i][1][0][0])
	for j in range(len(elem)):								
		element = driver.find_element_by_id("Gap" + str(j))	
		element.send_keys(Answers[j])						
	driver.execute_script("CheckAnswers()")				

def MultiChoiceBox(type,pageDesired):
	if type == "D":
		#Finds Multichoice boxes
		elem = []
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
		for j in range(len(elem)):		#For Each multichoice
			options.append(None)	
			complete = False		
			i = 0					
			while complete == False:	#While not all is found
				try:
					element = Select(driver.find_element_by_id("s"+str(j)+"_"+str(j)))		#Select the option with that number
					element.select_by_value(str(i))											
					options[j] = i+1														#Log that it can be done
					i +=1																	#
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
		for j in range(len(Answers[i])):
			if Answers[i][j][2] == 1:
				element = driver.find_element_by_id("Q_"+str(i)+"_"+str(j)+"_Btn")
				element.click()

def arrEqual(answers,options):
	for i in range(len(answers)):
		if answers[i]!=options[i]:
			return False
	return True

if __name__ == "__main__" :
	#Create Launch option parser
	parser = ArgumentParser(description='test', formatter_class=SmartFormatter)

	parser.add_argument('accname', metavar='username', type=str, help='the username of the desired account')
	parser.add_argument('accpass', metavar='password', type=str, help='the password of the desired account')
	parser.add_argument('url', metavar='url', type=str, help='the url of the activity')
	parser.add_argument('-t', choices=['t', 'g', 'd'], default='t', help="R|The type of activity, where\n" " t -> Tickbox based\n" " g -> Gap-fill based\n" " d -> Dropdown")

	args = parser.parse_args()

	activityType = args.t
	urldesired = args.url
	accname = args.accname
	accpass = args.accpass

	driver = webdriver.Chrome()
	pageDesired = init(urldesired,accname,accpass)
	Answers = []
	qNotType = []
	try:
		I = driver.execute_script("return I")
	except:
		I = None
	fqt = findQType(activityType)
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
	
