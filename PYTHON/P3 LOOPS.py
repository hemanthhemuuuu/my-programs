









#LAMBDA--SMALL ANONYM FUN() , TAKES ANY NO'S OF AGRUEMENTS BUT GIVES ONE EXPRESSION

#syn:: lambda arguements : exp


def m(n):
    return lambda a: a*n

s=m(int(input('enter no:')))
print(s(2))





x=lambda a:a+'hemu'
print(x('hello'))





#FIBONACCI SERIES

n=int(input('enter range:'))
a,b=0,1
for x in range(n):
    a,b=b,a+b
    print(a)
    print(x)



#LOOPS



#FOR LOOPS--EXECUTES A CODE FOR FIXED NO.OF TIMES
# WE CAN ITESRATE OVER A RANGE,STRING,SEQUENCE,ETC
#SYNTAX--   FOR variable IN   REVERSED(RANGE(START,END,STEP))

#continue--stops unlucky no. and loop will continue printing
#break----after the break to limit it won't contunue to print

#for x in range(1,20):
    if x==12:
        continue
    else:
        print(x)








#for x in reversed(range(1,21,2)):
#   print(x)








#WHILE LOOPS---EXEXCUTES WHILE CONDITION TRUE FOR INFINITY TIMES


#EX-3  SIMPEE INTREST

#AMOUNT=P*POW((1+R/N),T)

principle=float(input('enter the principle:'))

while principle<=0:
    print('must be greater than 0')
    principle=float(input('enter the principle:'))

print(f'{principle:.2f}')



#ex--2

num=int(input('enter the num:'))

while num<1 or num>10 :
    print(f' {num} is inavlid ')
    num=int(input('enter the another  num:'))

print(f'your num is {num}')




EX-1
name=input('enter the name:')

while name=='':
    print('not entered the name')
    input('enter the other name:')

print(f'hello {name}')
