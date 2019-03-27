import random 
from numpy.lib.function_base import average

caeser_questions = { 
    'Which answer is crypto put through a caeser cipher  ': 'jyfwav', 
    'Which answer is escape put through a caeser cipher  ': 'lzjhwl', 
    'Which answer is hacker put through a caeser cipher  ': 'ohjrly',  
    'Which answer is coding put through a caeser cipher  ': 'jvkpun'}   

questions = []  
unique_questions = []  
occurence_count = []


for i in range(0, 100):
    question = (random.choice(list(caeser_questions))) 
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
    

