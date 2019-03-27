import requests
import json 
import random  
from numpy.lib.function_base import average

questions = ['fred', 'bob', 'alice', 'eve'] 





questionst = []
unique_questions = [] 
occurence_count = [] 


for i in range(0, 100):   
    values = [] 
    question = (random.choice(questions)) 
    
    resp = requests.get('http://127.0.0.1:5000/question/' + question) 
    json_data = json.loads(resp.text)  
    if resp.status_code != 200: 
        print ("something went wrong") 
    for key, value in json_data.items(): 
        values.append(value)   
    user_question = values[1] 
    user_answer = values[0] 
        
    if questionst.__contains__(user_question): 
        occurence_count.append(question) 
    else:   
        unique_questions.append(user_question)  
    questionst.append(user_question) 
    
ocount = []     
        
print (len(questionst))  
print (len(unique_questions))       
        
for uquestion in unique_questions:  
    count = questionst.count(uquestion)  
    print('This question ' + uquestion + 'appeared  ' + str(count) + ' times') 
    ocount.append(count) 
    
print("There was a total of " + str(len(occurence_count)) + " Same occurences of a question")
print (str(average(ocount)))