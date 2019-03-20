from bs4 import BeautifulSoup 
import requests   
import random 
import hashlib 
import re 
from selenium import webdriver

source1 = requests.get('https://www.computersciencedegreehub.com/30-most-influential-computer-scientists-alive-today/').text
soup1 = BeautifulSoup(source1, 'lxml')  
 
people = [] 

for person in soup1.find_all('h3'):  
    computer_person = str(person).split('<h3>')  
    computer_person_name = str(computer_person).split('</h3>') 
    c = " ".join(re.findall("[a-zA-Z]+", str(computer_person_name)))   
    people.append(c) 
    
people.pop(34)
people.pop(33) 
people.pop(32) 
people.pop(31) 
people.pop(30) 
people.pop(0) 

person = (random.choice(people)) 
print (person + ' ' + hashlib.sha256(str(person).encode('utf-8')).hexdigest())
    
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome(options=options, executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", )
browser.get("https://passwordsgenerator.net/md5-hash-generator/") 
hashField = browser.find_element_by_id('txt1') 
hashField.send_keys(person)  
hashResult = browser.find_element_by_id('txt2').get_attribute("value")  
#hashField.send_keys(hashResult)  
print (person + ' ' + hashResult)