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
from numpy.lib.function_base import average 
from bs4 import BeautifulSoup 
import requests   
import random 
import hashlib 
import re 
from selenium import webdriver


subscription_key = "71ad32482bbb4d99a0882c34d8b08d9f"
search_term = "famous computer scientists" 


client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key)) 
image_results = client.images.search(query=search_term,count=100,ImageContent=face)  
   

from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome(options=options, executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", )

if image_results.value: 
    for i in range(0,100):
        first_image_result = image_results.value[i]
        browser.get(first_image_result.content_url)
    else:
        print("No image results returned!") 
        

    
    

        
 

        
  
    
 


    