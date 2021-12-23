#!/usr/bin/env python
# coding: utf-8

# # python
# ## 기본문법 1일차

# In[ ]:


print('hello')
print(10*20)
10+20


# In[ ]:


import keyword
#print(keyword.kwlist)


# In[ ]:


1 + 1


# In[ ]:


'hello'+' test'


# In[ ]:


print('test print')
print(10+20)


# In[ ]:


# print() 함수 사용해 보기
print("hello python")
print("연산식 :", 10+20)
print("여러자료 출력 : ", 10, 20, ' end')
print()
print(10+20)
print("test","123",sep='#')


# In[ ]:


# 자료형 확인
type('문자열')
print(type('abvd'))
print(type(12))
print(type(True))
print(type('10'))


# In[ ]:


abc = 10
abc


# In[ ]:


print("""안녕""")
# "을 출력하고자 할 때 "을 약속된 문자가 아닌 일반 문자로 인식을하고자 함
#  역 슬러시


# In[ ]:


# escape 를 활용한 탭 사용
print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사""")
print("""동해물과 백두산이 마르고 닳도록하느님이 보우하사""")
10 +20


# In[ ]:


#  문자열 연산자 : +,*
print("test"+" string")# test string
print("test "*3)# test test test


# In[ ]:


# 문자열 슬라이싱
print("hello test string"[0]) # h
print("hello test string"[-1])# g
print("hello test string"[:-3])# hello test str
print("hello test string"[6:])# test string
# print("hello str string"[20]) #error

print(len("hello str string"))
print("hello str string"[-3 : -1])
print("hello str string"[0:16])
print("hello str string"[1:15]) # 15 -> g // 출력 x


# In[ ]:


#  숫자 연산
print(10+20) # 30
print(10/3) #3.3..
print(10//3) # 몫의 정수만3
print(10%3) # 나머지 1
# print("test" + 3) #error
print(10**3) # 1000


# In[ ]:


# 변수 활용 변수명 = 값,, 변수는 방( 또는 박스)을 의미
pi = 3.14 # pi 라는 방을 만들고 방의 값은 3.14이다
print(pi) # 3.14
print(pi + 4) # 7.14
print(type(pi)) #float
pi = 'string test' # pi의 값은 'string test'로 변경됨
print(pi) # string test
print(type(pi)) # str

a = 'str'
a = 10
a = True
print("a : ", a, "type : ", type(a)) # True, boolean


# In[ ]:


number = 100
number += 10
number +=20
number +=30
print("number:",number)
string = "hello"
string += "!"
print("string : ",string)


# In[ ]:


# input 함수
string = input(" input data > ") # 들어온 데이터를 다 문자로 인식


# In[ ]:


# string = int(string) + 10
string += '10'
string # 문자를 숫자로 변경 int(변수명 또는 문자), float(문자)
#숫자를 문자로 변경 str(숫자)
str(string) + 'test'


# In[ ]:


# 문자열 관련 함수 : format
a_str = "{} test {}".format(10, 'add')
print(a_str)
print("{:d} {:f} {:.3f}".format(10,10.0,10.0))


# In[ ]:


format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a, format_b, format_c, format_d)


# In[ ]:


output_a = "{:d}".format(52)
b = "{:05d}".format(52)
c = float("{:5d}".format(-24))
print(output_a, b, c)
type(c)
str(b)
print(type(b))


# In[ ]:


# 문자열 관련함수 : upper(), lower(), strip(), lstrip(), rstrip()
a_str = "   test str 10 num ABc test DEf   "
print(a_str.upper())# 모두 대문자로
print(a_str.lower())# 모두 소문자로
print(a_str.strip())# 양쪽 공백제거
print(a_str.lstrip())#왼쪽 공백제거
print("/",a_str.rstrip(),"/")#오른쪽 공백 제거
print("/{}/".format(a_str.strip()))

print(a_str.strip()[:4].isalnum()) #True //isalnum() : 알파벳과 숫자만 있는가? / [:4]-> (0,1,2,3)
print(a_str.strip().isalnum()) #False


# In[ ]:


print(a_str.find('test')) # 인덱스(주소) 반환
print(a_str.rfind('test')) # 인덱스(주소) 반환 (뒤 부터 찾음)
print('test' in a_str) #True '문자' in "문자열" -> 문자가 문자열에 존재시 True


# In[ ]:


# 문자열 관련함수
# format ,lower, upper ,strip, is00,in, find, rfind
#string.함수명()
# split() : 문자열 자르기 -> 리스트로 반환
print(a_str.split())
a_str.split(sep = ' ')
a_list = a_str.split()
print(type(a_list),type(a_list[0]))
# a_str = "   test str 10 num ABc DEf   "
a_list[0][0]# a_list 의 처음 자료를 검색후 처음 자료의 첫글자 출력
a_list[3][1:-1] # [3]-> num [1:-1] -> 1:u , -1:m


# In[ ]:


# 두 수를 입력받아 두 수의 합과 차를 구하세요
a_str= input("두 수 입력 >")
a_list = a_str.split()
a_1 = int(a_list[0])
a_2 = int(a_list[1])
print(a_1 + a_2, a_1 - a_2)


# In[ ]:


# teacher
input_data = input("두 수 입력> ").split()
input_num1 = int(input_data[0])
input_num2 = int(input_data[1])
print("{}+{}={}".format(input_num1, input_num2,input_num1 + input_num2))
print("{}-{}={}".format(input_num1, input_num2,input_num1 - input_num2))


# In[ ]:


# 영문자를 입력받아 변수에 저장한 후 대문자, 소문자로 출력하세요
#isalpha 가 true인지 확인하세요
#숫자를 입력받아 변수에 저장한 후 isdigit를 확인하세요
#문자를 10개 입력받아 변수에 저장한 후 5번째 문자열의 처음 문자만 출력
#문자열의 길이를 출력하세요
#문자에 'test'가 입력 되었는지 확인하세요
#숫자 세개를 입력 받아 처음 숫자와 마지막 숫자의 합구하시오
# 두번째 숫자와 마지막 숫자의 곱을 구하시오


# In[ ]:


# 영문자를 입력받아 대문자 소문자 출력, isalpha 가 true 인지 확인
input_data = input("문자 입력>")#split을 사용하면 안됨
a = input_data.upper()
b = input_data.lower()
print(a)
print(b)
print("isalpha : {}".format(input_data.isalpha()))


# In[ ]:


#숫자를 입력받아 isdigit확인, 숫자 세개 입력 받아 처음 숫자와 마지막 숫자 합, 두번째 숫자와 마지막 숫자 곱
input_data2 = input("숫자 입력>").split()
print("numper ? {}".format(input_data2[0].isdigit())) # isdigit은 문자열에만 사용
data1 = int(input_data2[0])
data2 = int(input_data2[1])
data3 = int(input_data2[2])
print("{}+{}={}".format(data1, data3, data1+data3))
print("{}*{}={}".format(data2,data3,data2*data3))


# In[ ]:


# 문자를 5개 입력받아 변수에 저장한 후 3번째 문자열의 처음 문자만 출력
input_str = input("input string > ").split()
print("3번째 문자열의 처음 문자 : {}".format(input_str[2][0]))
#5번째 문자의 마지막 문자만 출력
print("5번째 문자열의 처음 문자 : {}".format(input_str[-1][-1]))


# In[ ]:


# 문자열의 길이를 출력하세요
print(len(input_str))
#문자에 'test'가 입력되었는지 확인하기
print('test' in input_str)


# In[ ]:


# 영문자를 입력받아 변수에 저장한 후 대문자, 소문자로 출력하세요
#isalpha 가 true인지 확인하세요
#숫자를 입력받아 변수에 저장한 후 isdigit를 확인하세요
#문자를 10개 입력받아 변수에 저장한 후 5번째 문자열의 처음 문자만 출력
#문자열의 길이를 출력하세요
#문자에 'test'가 입력 되었는지 확인하세요
#숫자 세개를 입력 받아 처음 숫자와 마지막 숫자의 합구하시오
# 두번째 숫자와 마지막 숫자의 곱을 구하시오
alpha = input("영문자를 입력하시오>")
print(alpha.upper())
print(alpha.lower())
beta = input("영문자를 입력하시오2>").split()
print(len(beta))
print("마지막 문자열의 처음 문자 : {}".format(beta[-1][0]))
print("3번째 문자열의 처음 문자 : {}".format(beta[2][0]))
print('test'in beta)
c = input("숫자를 입력하시오").split()
num1 = int(c[0])
num2 = int(c[1])
num3 = int(c[2])
print("숫자 ? : {}".format(c[0].isdigit()))
print("{}+{}={}".format(num1,num3,num1+num3))
print("{}*{}={}".format(num2,num3,num2*num3))


# In[ ]:




