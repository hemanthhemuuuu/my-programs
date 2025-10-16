


#MEMBERSHIP OPERATOR--TO KNOW THE VALUE IS THERE OR NOT SEQUENCE
#in
#not in strings ,tuples ,dictionary ,set,lists


#DICTIONARY

d={'a':4,
   'b':8,
   'c':12,
   'd':16}
ch=input('enter ch:')
if ch in d:
     print(f'{ch} is found in {d[ch]}')
else:
     print(f'{ch} not in there')



#SETS

set={'a','b','c','d'}

ch=input('enter ch:')
if ch in set:
     print(f'{ch} is found in')
else:
     print(f'{ch} not in there')



#STRINGS


w='ALLPE'

let=input('enter letter:')

if let in w:
        print(f'{let} is there')
else:
        print(f'{let} is not found')







#ITERABLES--An iterable is any Python object capable of returning its members one at a time, allowing it to be iterated over in a loop (like a for loop).

d={'n':4,
   'nm':8,
   'h':16,
   'd':28}

for x, y in d.items():
        print(f'{x} : y')


#STRINGS

n='hemu buddi'
for x in n:
        print(x)


#SETS

fru={'apple','banana','carrot'}
for x in fru:
        print(x)


#LISTS & TUPPLE

n=(1,2,3,4,5)
for x in n:
        print(x)






#ARBITARY ARGUEMENTS--VARYING AMOUNT OF ARGUEMENTS
           #*args---MULTIPLE NON-KEY ARGUEMENTS
            #*kwargs--MULTIPLE KEYWORD ARGUEMENTS


#EX----USING BOTH *ARGS AND *KWARGS

def boat(*args,**kg):
        for arg in args:
            print(arg,end=' ')
        print()

        for k,v in kg.items():
            print(f'{k}:{v}')
            print()

        print(f'{kg.get('N')}')
        print(f'{kg.get('NI')}')
        print()
        print(f'{kg.get('H')}')
        print()
        print(f'{kg.get('D')}')
boat('I','AM','HEMU','SHE','IS','BUDDI',
     N='NAGALINGAMU',
     NI='NIRMALA DEVI',
     H='HEMANTH KUMAR',
     D='DEEPIKA')


#**KWARGS---DICTIONARY

def add(**kwargs):
    for key,val in kwargs.items():
        print(f'{key}:{val}')


add(c='stp',s='ap',d='Ind',pin='515511')


#FOR NAME BY *args--TUPPLE

def name(*hems):
    for hem in hems:
        print(hem,end=' ')

name('HEMU','BUDDI')



          
def add(*args):
    total=0
    for x in args:
        total+=x
    return total

print(add(1,2,3,4))






#3--KEYWORD ARGUEMENTS ---AN ARGUMENT PRECEEDED BY AN IDENTIFIER
                        #HELPS WITH REDABILITY
                        #ORDER OF ARGUMENTS DOEN'T MATTER


def fill(cou,area,f,l):
    return f'{cou}-{area}-{f}-{l}'

ph=fill(cou='india',f='86396',l='98826',area='GVP')
print(ph)



#EX ----

print('1','2','3','4',sep=" ")


for x in range(0,11):
    print(x,end=" ")


def hello(gret,title,f,l):
    print(f'{gret} {title} {f} {l}')
    
hello('mrs.','buddi','hello','hmeu') 




#RETUN --STATEMENT USED TO END A FUN()
#RETRNS  A VALUES
#WHEN WE HAVE RETURN WE PRINT OUTPIT AT INVOKE FUN OR WHERE WE ARE GIVING INPUTS

#EXERCISE-DEFAULT ARGUMENTS
import time
def c(end,s=0):
    for x in range(s,end):
        print(x)
        time.sleep(0.0001)

    print('DONE!!')

c(10)


          

#////////DEFAULT //////

def n(name,bal=500):
    print(f"my name is {name}")
    print(f'my bank bal is {bal}')
    
n('hemu')




#////POSITIONAL --DEFAULT ARGUEMENTS

def name(f,l):
    f.capitalize()
    l.capitalize()
    n=f+" "+l
    return n

print(name(input('enter f:'),input('enter l:')))
