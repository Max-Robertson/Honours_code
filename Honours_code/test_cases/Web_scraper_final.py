from bs4 import BeautifulSoup 
import requests   
import random 
import hashlib 
import re 
from selenium import webdriver
from numpy.lib.function_base import average

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


questions = []  
unique_questions = [] 
occurence_count = []

for i in range(0, 100):
    question = (random.choice(people))
    if questions.__contains__(question): 
        occurence_count.append(question)  
    else:   
        unique_questions.append(question)  
    questions.append(question)     
        
print (len(questions))  
print (len(unique_questions))   

ocount = []     
        
for uquestion in unique_questions:  
    count = questions.count(uquestion)  
    print('This question ' + uquestion + ' appeared  ' + str(count) + ' times') 
    ocount.append(count)
print("There was a total of " + str(len(occurence_count)) + " Same occurences of a question") 
print (str(average(ocount)))


