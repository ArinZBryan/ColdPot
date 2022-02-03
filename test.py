
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
	pageDesired = e.gap
	
	driver.get("https://vle.rgshw.com/index.php")
	element = driver.find_element_by_id("username")
	element.send_keys(userDesired)
	element = driver.find_element_by_id("password")
	element.send_keys(passDesired, Keys.ENTER)
	driver.get("https://vle.rgshw.com/course/view.php?id=3004")
	driver.get(pageDesired)
	return pageDesired

driver = webdriver.Chrome()
pageDesired = init()
complete = False
i = 0
elem = []

#Finds Multichoice boxes
while complete == False:
	try:
		element = Select(driver.find_element_by_id("Gap"+str(i)))
		elem.append(element)
		i += 1
	except:
		complete = True
"""
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
driver.execute_script("CheckAnswers()") """

def arrEqual(answers,options):
	for i in range(len(answers)):
		if answers[i]!=options[i]:
			return False
	return True
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
	#Gap
else:
	if arrEqual(answers,options) == True:
		#MCBc
		pass
	else:
		#MCBa
		pass

try:
	driver.find_element_by_id("Questions")
	try:
		driver.find_element_by_id("ShowMethodButton")
		##MCc
	except:
		pass
		##MCBd
except:
	pass
try:
	gSpan = driver.find_elements_by_id("GapSpan")
except:
	pass
try:
	gBox = driver.find_elements_by_class_name("GapBox")	
except:
	pass
try:
	qs = driver.find_element_by_id("Questions")
except:
	pass
try:
	tf = driver.find_element_by_id("ShowMethodButton")
	tf.click()
except:
	pass
