

#DEFAULT ARGUMENTS ----DEFAULT FOR CERTAIN PARAMETERS

#///////////////DEFAULT ARGUEMENTS/////////////////////\\\\\

import time

def count(end,start=0):
    for x in range(start,end):
        print(x)
        time.sleep(0.01)
    print('!WORK DONE!!')
        
count(30,15)      






def net(pri,dis=0,tax=0.05):
    return pri*(1-dis)*(1+tax)

#print(net(100))
#print(net(100,0.1))
print(net(100,0.1,0))









#RETURN ---STATEMENT USED TO END A FUN()
        #RETURNS A VALUE BACK TO THE CALLER

#           (((({{{{{ POSITIONAL))))}}}



def cre_name(f,l):
    f=f.capitalize()
    l=l.capitalize()
    return f+"  "+l
     
p=cre_name(input('enter f:'),input('enter l:'))
print(p)








def add(a,b):
    z=a+b
    return z
def sub(a,b):
    z=a-b
    return z
def mul(a,b):
    z=a*b
    return z

print(add(2,4))
print(sub(1,2))
print(mul(1,2))











#FUNCTIONS ---A BLOCK OF REUSABLE CODE PLACE () AFTER THE FUN_NAME TO INVOKE IT


#EXERCISE 1--

def dis_in(name,amount,date):
    print(f'my name is {name}')
    print(f'my  bank balance is :{amount}')
    print(f'date to pay is:{date}')

dis_in(input("enter the name:"),input("enter the amount:"),input("enter the date:"))
print()












def fun_name(name,age):
    print(f"I AM {name}:{age}")
    print("YOU ARE BUDDI")
    print("WE ARE FAMILY")
    print()

fun_name('hemu',16)
fun_name('buddi',28)





def fun_name():
    print("I AM HEMU")
    print("YOU ARE BUDDI")
    print("WE ARE FAMILY")
    print()

fun_name()
fun_name()
