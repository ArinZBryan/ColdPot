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

driver = webdriver.Chrome()
pageDesired = init()
complete = False
i = 0
elem = []
while complete == False:
	try:
		element = Select(driver.find_element_by_id("s"+str(i)+"_"+str(i)))
		elem.append(element)
		i += 1
	except:
		complete = True
complete = False
j = 0
answers = []
for i in range(len(elem)):
	while complete == False:
		try:
			elem[i].select_by_value(str(j))
			try:
				element = driver.find_element_by_id("FeedbackOKButton")
				element.click()
				answers.append(j)
			except:
				j+=1
		except:
			complete = True
while complete == False:
	try:
		element = Select(driver.find_element_by_id("s"+str(i)+"_"+str(i)))
		element.select_by_value(str(answers[i]))
		i += 1
	except:
		complete = True
print("")