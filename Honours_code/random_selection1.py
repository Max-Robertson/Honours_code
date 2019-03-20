import random

caeser_questions = { 
    'Which answer is crypto put through a caeser cipher  ': 'jyfwav', 
    'Which answer is escape put through a caeser cipher  ': 'lzjhwl', 
    'Which answer is hacker put through a caeser cipher  ': 'ohjrly',  
    'Which answer is coding put through a caeser cipher  ': 'jvkpun'}  

question = (random.choice(list(caeser_questions)))
print(question)

for key, value in caeser_questions.items(): #its data.items() in Python 3.x
    print ("---" + value) 
   
answer = input("Enter answer here:") 

def checkAnswer(caeser_questions, answer): 
    correctAnswers = "" 
    listOfItems = caeser_questions.items() 
    for item  in listOfItems:
        if item[1] == answer:
            correctAnswers = item[0] 
    return  correctAnswers 

answerChecked = checkAnswer(caeser_questions, answer)  


if (answerChecked == question): 
    print ("correct")  
else: 
    print ("incorrect")