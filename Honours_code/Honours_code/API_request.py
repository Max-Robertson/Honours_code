import requests
import json 
import random  

questions = ['fred', 'bob', 'alice', 'eve'] 
question = (random.choice(questions)) 
values = []

resp = requests.get('http://127.0.0.1:5000/question/' + question) 
json_data = json.loads(resp.text) 
if resp.status_code != 200: 
    print ("something went wrong") 
for key, value in json_data.items(): 
    values.append(value)  
user_question = values[1] 
user_answer = values[0]   
txt = input(user_question)
if (txt == user_answer): 
    print ("correct !")  
else:
    print ("incorrect")