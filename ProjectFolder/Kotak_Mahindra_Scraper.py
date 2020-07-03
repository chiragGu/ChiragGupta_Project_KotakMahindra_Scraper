#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 12:47:49 2020

@author: chirag
"""

from bs4 import BeautifulSoup
import requests
import json



url ="https://happycredit.in/kotak-mahindra-bank-offers/"
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

Offers=[]


for data in content.find_all('a', attrs={"class": "coupon-cart others"}):
    Offer=[]
  
    p1 = data.find('h3').text           # Gets the header of the offer 
    #print("*****right-clm" + p1)       # To check the header output
        
    
    p2 = data.find('p', attrs={"class":"info-txt"}).text  # Gets the offer message
    #print("$$$$$Info-txt"+ p2)
    
    x1=[]
    for p3 in data.find('div', attrs={"class": "info"}).find('p'):  # Gets the info regarding offer such as By, Valid till, Bank, Deal Type, Card Type 
        x1.append(p3.text)                                          # All the details are appended in a list x1
    
    Offer.append("OfferName: " + p1)

        
    for i in range(len(x1)):            
        Offer.append(x1[i])

    
    Offer.append("OfferMessage: "+ p2)   
    
    print(Offer)                        # Offers are printed 
    
    
    Offers.append(Offer)                # All the generated offers are compiled together

with open('Chirag-Gupta-Kotak-Mahindra-Scrap.json', 'w') as outfile:
    json.dump(Offers, outfile)          # Stored in a Json file 
    
  