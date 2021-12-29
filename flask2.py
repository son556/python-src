#!/usr/bin/env python
# coding: utf-8

# In[15]:


from flask import Flask
from urllib import request #1
from bs4 import BeautifulSoup


app = Flask(__name__)
@app.route('/')
def hello():
    url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId=108'
    target = request.urlopen(url)
    soup = BeautifulSoup(target)
    
    output = " "
    for location in soup.find_all('tr'):
        if location.find('td',class_='midterm-city'):
            output += "<h3>{}</h3>".format(                                           location.find('td',class_='midterm-city').text)
                                                
            output += "최저/최고 기온: {}/{}".format(                                               location.find('span',class_='tmn').text,                                              location.find('span',class_='tmx').text)
    output += '<hr/>'
    print(output)  
    return output
hello()

