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
	pageDesired = e.MCBc
	
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

try:
	elem = driver.find_elements_by_class_name("GapSpan")			#Current MultiChoice Format
except:
	qType = "MCBd"

try:
	elem = driver.find_elements_by_class_name("Gap0")
	options = [x for x in elem.find_elements_by_tag_name("option")]
	i = driver.execute_script("return I[0][1]")
	
except:

print(qType)