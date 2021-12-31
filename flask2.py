#!/usr/bin/env python
# coding: utf-8

# In[23]:


from flask import Flask
from urllib import request #1
from bs4 import BeautifulSoup
city_list = []
output_1 = []
output_2 = []
output_3 = []
temp_list = []
w_dict = {}
app = Flask(__name__)
@app.route('/')
def hello():
    url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId=108'
    target = request.urlopen(url)
    soup = BeautifulSoup(target)
    
    output = " "
    for location in soup.find_all('tr'):
#         output = " "
        if location.find('td',class_='midterm-city'):
            output_1_1 = "<h3>{}</h3>".format(                                           location.find('td',class_='midterm-city').text)
            city_list.append(location.find('td',class_='midterm-city').text)
            output_1.append(output_1_1)
            
            output_3_3 = "최저/최고 기온: {}/{}".format(                                            location.find('span',class_='tmn').text,                                            location.find('span',class_='tmx').text)
            output_3.append(output_3_3)
            
        if location.find('td') and location.select_one('img'):
#             print(location)
            data = location.select_one('img').attrs['title']
            temp_list.append(data)
            
#   도시와 날씨의 짝을 맞춰주는 부분. // 실시간 데이터 받기   
    for i in range(0,6): 
        w_dict[city_list[i]]=temp_list[0]
    for i in range(6,8):
        w_dict[city_list[i]]=temp_list[1]
    for i in range(8,9):
        w_dict[city_list[i]]= temp_list[2]
    for i in range(9,12):
        w_dict[city_list[i]]= temp_list[3]
    for i in range(12,15):
        w_dict[city_list[i]]= temp_list[4]
    for i in range(15,21):
        w_dict[city_list[i]]= temp_list[5]
    for i in range(21,27):
        w_dict[city_list[i]]= temp_list[6]
    for i in range(27,33,1):
        w_dict[city_list[i]]= temp_list[7]
    for i in range(33,39,1):
        w_dict[city_list[i]]= temp_list[8]
    for i in range(39,41,1):
        w_dict[city_list[i]]= temp_list[9]
    for key, value in w_dict.items():
        output_2_2 = "<h4>날씨 {}</h4>".format(value)
        output_2.append(output_2_2)
    for idx, value in enumerate(output_1):
        output += output_1[idx]
        output += output_2[idx]
        output += output_3[idx]
    return output
hello()

