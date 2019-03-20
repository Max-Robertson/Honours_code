
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
import pymongo 
#from flask_pymongo import PyMongo


#topics = ['Famous Computer Scientists', 'Famous Cryptographers', 'Famous tech People', 'famous cryptologists', 'famous computer programmers' , 'top cryptocurrency pioneers']
topics = ['Movie Stars', 'A list movie stars', 'Famous Actors', 'Tv stars', 'Famous Tv actors' , 'Movie Directors']


subscription_key = "71ad32482bbb4d99a0882c34d8b08d9f"
search_term = random.choice(topics)   

headers = {
    # Request headers. Replace the key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9a899136784940ebadbe150dc9d28b39',
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories',
    'details': 'Celebrities',
    'language': 'en',
}) 

myclient = pymongo.MongoClient("mongodb://localhost:53244/")  
#myclient = pymongo.MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
mydb = myclient["mydatabase"]
mycol = mydb["challenges"]

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
        #print(search_term)
        text = findImages(subscription_key, search_term)  
        body = "{'url':\'"+text+"\'}" 
        #print (text)  
        h1 = http.client.HTTPConnection('www.cwi.nl')
        conn = http.client.HTTPConnection('northeurope.api.cognitive.microsoft.com') 
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers) #
        response = conn.getresponse() 
        data = response.read() 
        conn.close() 
        d1=json.loads(data)    
        #print(data)
        #if (str(data).__contains__('"celebrities":[]' or 'categories":[]')): 
        if (str(data).__contains__('"celebrities":[]') or str(data).__contains__('"categories":[]')):  
           # print ("catching empties has worked")
            return("no match");    
        else:  
            name = (d1['categories'][0]['detail']['celebrities'][0]['name']) 
            score = (d1['categories'][0]['detail']['celebrities'][0]['confidence']) 
            classification = (d1['categories'][0]['name'])       
        try:
            urllib.request.urlretrieve(text) 
        except urllib.error.HTTPError:  
           # print("http error handling has worked")
            return("no match")    
        

        if name == "":  
           # print("name is empty so failed")
            return("no match");  
        elif score == "":  
           # print("score is empty so failed")
            return("no match");  
        elif (classification == "people_" or classification == "people_portrait"):   
            #print (classification + " has passed the classification test and is therefore equal to people_ or people_portrait") 
            mydict = { "question": "Who is this ?", "image":text, "name":name} 
            x = mycol.insert_one(mydict) 
            print("Data has been inserted to database")
            return (text);  
        else:  
           # print (classification + " has failed the classification test and is therefore not equal to people_ or people_portrait")
            return("no match");
        
        #if not (('"celebrities":[]' or 'categories":[]') in str(data)) or text:    
    except KeyError:   
        #print("Failed because of exeption")
        return("no match");  
    


while True:  
    text = findMatch()
        
    if text != "no match": 
        break   
    

    

    
