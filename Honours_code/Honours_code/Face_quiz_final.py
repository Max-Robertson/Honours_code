import http.client, urllib, base64
from pprint import pprint 
import json
import sys 
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials  
from PIL import Image 
import urllib.request  
import urllib.error
import os  
import random
from cognitive_face import face
from azure.cognitiveservices.search.imagesearch.models.image_search_api_enums import ImageContent



topics = ['Famous Computer Scientists', 'Famous Cryptographers', 'Famous tech People', 'famous cryptologists', 
          'famous computer programmers' , 'top cryptocurrency pioneers']



subscription_key = "71ad32482bbb4d99a0882c34d8b08d9f"
search_term = random.choice(topics)   

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9a899136784940ebadbe150dc9d28b39',
}

params = urllib.parse.urlencode({
    'visualFeatures': 'Categories',
    'details': 'Celebrities',
    'language': 'en',
})

def findImages (subscription_key, search_term):

    client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key)) 
    image_results = client.images.search(query=search_term,count=100,ImageContent=face) 

    if image_results.value:
        first_image_result = random.choice(image_results.value)  
        return(first_image_result.content_url); 

    else:
        print("No image results returned!") 
    
    



def findMatch (): 
    try:    
        search_term = random.choice(topics) 
        text = findImages(subscription_key, search_term)  
        body = "{'url':\'"+text+"\'}" 

        h1 = http.client.HTTPConnection('www.cwi.nl')
        conn = http.client.HTTPConnection('northeurope.api.cognitive.microsoft.com') 
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers) #
        response = conn.getresponse() 
        data = response.read() 
        conn.close() 
        d1=json.loads(data)     
         
        if (str(data).__contains__('"celebrities":[]') or str(data).__contains__('"categories":[]')):  
            #print ("catching empties has worked")
            return("no match");    
        else:  
            name = (d1['categories'][0]['detail']['celebrities'][0]['name']) 
            score = (d1['categories'][0]['detail']['celebrities'][0]['confidence']) 
            classification = (d1['categories'][0]['name'])       
        try:
            urllib.request.urlretrieve(text, r"C:\Users\MAXBO\Documents\Test_images\file1.jpg")  
            os.chdir(r'C:\Users\MAXBO\Documents\Test_images') 
        except urllib.error.HTTPError:  
            #print("http error handling has worked")
            return("no match")    
        

        if name == "":  
            #print("name is empty so failed")
            return("no match");  
        elif score == "":  
            #print("score is empty so failed")
            return("no match");  
        elif (classification == "people_" or classification == "people_portrait"):   
            #print (classification + " has passed the classification test and is therefore equal to people_ or people_portrait")
            return (text);  
        else:  
            #print (classification + " has failed the classification test and is therefore not equal to people_ or people_portrait")
            return("no match");
        
    except KeyError:   
        #print("Failed because of exeption")
        return("no match");  
    
def getAnswer():
    try:   
        h1 = http.client.HTTPConnection('www.cwi.nl')
        conn = http.client.HTTPConnection('northeurope.api.cognitive.microsoft.com') 
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers) #
        response = conn.getresponse() 
        data = response.read() 
        conn.close() 
        d1=json.loads(data)   
        #if (str(data).__contains__('"celebrities":[]' or 'categories":[]')):     
        score = (d1['categories'][0]['detail']['celebrities'][0]['confidence']) 
        percentage = (score * 100) 
        rounded_percentage = round(percentage,2)  
        name = (d1['categories'][0]['detail']['celebrities'][0]['name']) 
        urllib.request.urlretrieve(text, r"C:\Users\MAXBO\Documents\Test_images\file1.jpg")  
        os.chdir(r'C:\Users\MAXBO\Documents\Test_images')
        im = Image.open(r"C:\Users\MAXBO\Documents\Test_images\file1.jpg")  
        im.show()
        answer = input("Who is this ?") 
        if (answer.lower() == name.lower()): 
            return("Correct, I am " + str(rounded_percentage) + " the correct answer is " + name); 
        else: 
            return("Incorrect, I am " + str(rounded_percentage) + " the correct answer was " + name);

    except KeyError:  
        return("Error has occured. Try again.") 
 
correct_answers = 0  
        
for i in range(0, 5):
    while True:  
        text = findMatch()
        
        if text != "no match": 
            break   
    
    body = "{'url':\'"+text+"\'}"  

    print("Person " + str(i+1) + ":" )
    answer = getAnswer() 
    if answer == "correct": 
        correct_answers = correct_answers + 1  
    print(answer)  
        
print("You scored " + str(correct_answers) + "/5")
    
