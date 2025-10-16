
#FORMAT SPECIFICATIONS--DECIMAL POINTS,PUTTING ,><+-


p1=99999
p2=-88888
p3=4444.44

#print(f'price:{p1:.2f,<>+-}')






#INDEXING--ACCESSSING THE ELEMENTS OF A SEQUENCE USING []

#ph=(input('enter the number:'))
#res=ph[0:9:2]   #[start:end:step]
#print(res)

#for reversing of a string ==ph[::-4]





#STRING METHODS EXERCSE
#USER NAME NO MORE THAN 12 CHARACTERS
#USER MUST NOT CAONTAIN SPACES
#USER NAME MUST NOT CONTAIN DIGITS


#username=input('enter user name:')

#if len(username)>12:
 #   print('your name shuold contail 12 characters only')
#elif not username.find(' ')==-1:
 #   print('no spaces contain')
#elif not username.isalpha():
 #   print("you are welcome")








#STRING METHODS

name=input('enter the name:')

#res=len(name)
#res=name.find('h')
#res=name.rfind('a')
#res=name.lower()
#res=name.upper()
#res=name.capitalize()
#res=name.title()
#res=name.swapcase()
#res=name.isdigit()
#res=name.isalpha()
#res=ph.count("-")
#res=ph.replace("-"," ")
#res=name.isalpha()
res=name[::-1]
print((res))










#CONDITIONAL EXPRESSIONS ::::A 1 LINE SHORTCUT FOR IF-ELSE STATEMENT

num=21
a=1
b=2

#print("pos" if num>0 else "neg")

#res=num%2
#print("even" if res==0 else "odd")

max=print("a" if a>b else "b")

min=print("a" if a<b else "b")


#LOGICAL OPERATIONS (AND,OR,NOT)


#AND--BOTH STATEMENTS MUST BE TRUE 
#OR--ONE OF THE STATEMENTS MUST BE TRUE 
#NOT--IT SHOWS THE STATEMENTS IS FALSE AS NOT ///// INVERTS THE CONDITION NOT TRUE NOT FALSE 

temp=40
sun=True


if temp<=30 or not sun:
    print('sunny day')
elif temp>50 or not sun :
    print('coldy')
else:
    print('windy  day')




if temp>=30 and sun:
    print('sunny day')
elif temp<50 and sun:
    print('coldy')
else:
    print('windy  day')






# EXERCISE:::::  TEMPEARTURE CONVERTER PROGRAM 

op=input('enter the option:(c/f):')
temp=float(input('enter the temp:'))

if op=='c':
    res=temp*32
    units='f*'
    print(f'the temp is {res}{units}:   ')
elif op=='f':
    res=temp/32
    units='c*'
    print(f'the temp is {res}{units}:   ')
else :
    print(' no such option')







#WEIGHT CONVERTER PROGRAM
#POUNDS---->KGS=POUNDS/2.205
#KGS----->POUNDS=KGS*2.205


#USINF CONDITIONAL STATEMENTS









#PYTHON CALCULATOR

ch=input('enter your ch:(+ - * /%):')
n1=float(input('enter n1:'))
n2=float(input('enter n2:'))

if ch=='+':
    res=n1+n2
    print(res)

elif ch=='-':
    res=n1-n2
    print(res)

elif ch=='*':
    res=n1*n2
    print(res)

elif ch=='/':
    res=n1/n2
    print(res)
else :
    res=n1%n2
    print(res)







#CONDITIONAL STATEMENTS ::IF ELIF ELSE
#IF CONDITION TRUE S ELSE IT'S FALSE


####RESPONSE FROM CUSTMERS

res=input('enter your res:(s/n)')          #when we have 2 values then we use
                                           # assignment operator
if res=='s':
    print('you can take food')
else :
    print('you are not allowed to take it')






#USING BOOLEN EXPRESSIONS

age=10

if age:
    print('yes')
else:
    print('nooo')





age=int(input('enter your age:'))

if age>18:
    print('you can sign up')
elif age<18:
    print('you are not eligible')
elif age>100:
    print('you are too old too sign up')
else:
    pritf("you are not able to sign up")








#C=SQRT(A)+SQRT(B)

import math

a=float(input('enter a :'))

b=float(input('enter b :'))

c=math.sqrt(pow(a,2)+pow(b,2))
print(f'the answer ={c}')










#AREA OF A CIECLE PI *R*R

import math

r=float(input('enter radius of  a circle:'))
area=math.pi*pow(r,2)
print(f"THE AREA OF CIRCLE IS:{round(area)}")






#CALCULATE THE CIRCUMFERENCE OF A CIRCLE(2*PI*R)

import math

r=float(input('enter radius of  a circle:'))
c=2*math.pi*r
print(f'THE CIRCUMFERENCE IS :{(c)}')










 #IMPORT MATHEMATICAL CONSTANTS


#IMPORT USE::::Tells Python to load the built-in math module, which includes a collection of mathematical functions and constants

import math

x=9.1

#print(math.pi)

#print(math.e)

#res=math.sqrt(x)

#res=math.ceil(x)   ____IT SHOWS THE MAX VALUE OR APPROXIMATE VALUE

#res=math.floor(x) ____SHOWS THE MIN VALUE OF DECEMAL NO.

#print(res)
