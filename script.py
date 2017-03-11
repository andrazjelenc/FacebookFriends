from selenium import webdriver
from time import sleep
import codecs

def getDocHeight(b):
	return b.execute_script('return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight)')

def scrollDown(b):
	b.execute_script('window.scrollTo(0,document.body.scrollHeight);')

def getHtml(b, id):
	b.get('https://facebook.com/' + id)
	try:
		vrstica = b.find_element_by_id('fbTimelineHeadline') #vrstica z gumbi
		gumb = vrstica.find_element_by_xpath("//*[@data-tab-key='friends']") #gump za na friends
		gumb.click()
		sleep(4)
		gumb2 = vrstica.find_element_by_xpath("//*[@name='Mutual Friends']") #gumb skupni prjatli
		gumb2.click()
	except:
		print("Uporabnika NI")
		return "-1"
	
	#scrollamo do dna
	visina = 0
	counter = 0
	while(counter < 4):
		print("scrollam...")
		scrollDown(b)
		novaVisina = getDocHeight(b)
		#print(novaVisina)
		if(novaVisina == visina):
			counter += 1
		else:
			counter = 0
			visina = novaVisina
			
		
		sleep(3)
	
	return b.page_source
 
 
b = webdriver.Chrome()
b.get('https://www.facebook.com')

input("Prijavite se! Press ENTER to continue")

file = open('error2.txt', 'r')

for line in file.readlines():
	print ("Prenos prijateljev osebe: " + str(id))
	id = line.strip()
	html = getHtml(b, id)
	#input("hahahhahaha")
	if(html == "-1"):
		continue
	
	output = codecs.open('friends\\' + id + '.txt', 'w+', 'utf-8') 
	output.write(html)
	output.close()

file.close()
