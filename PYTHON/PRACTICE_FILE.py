
#ACCESSING NUM USING NESTED LOOPS

n=5

for i in range(n):
        for j in range(i):
                if i%2==0:
                        print('1',end=' ')
                else:
                        print('2',end=' ')
        print()       
       







t=int(input())
for _ in range(t):
        n=int(input())
        if t<=10:
            print('yes')
        else:
            print('no')


def m(*hem):
      total=0
      count0
      for x in hem:
            total+=int(x)
            count+=1

marks=input('enter marks:').split()
m(marks)



#JOING TO SETS USING---UNION()

h={'a','b','c'}
b={1,2,3}
n={'@','#','$'}

#set3=h.union(b)
#set3=h|b
#mul=h.union(b,n)
mul=h|b|n
for s in mul:
      print(s)














#USED SETS ND SICTIONARY CONCPETS
d={'a':1,
   'b':2,
   'c':3}

print("------MENU-----")
cart=[]
total=0
for key,val in d.items():
     print(f'{key:}:{val}')


while True:
  food=input('enter the food(q to quit):').lower()
  if food=='q':
    break
  elif d.get(food) is not None:
    cart.append(food)
for food in cart:
     print(f'{food}')
   
     
     total +=d.get(food)
print(f'YOUR TOTAL COST IS :{total}')



#SETS 

s={'a','b','c'}
p={'e','f','g'}
s.update(p)
print(p)

#for c in s:
 #     print(c)

#for c in s:
 #    print('c' in c)








#LISTS


mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):

  print(mylist[i])
  i = i + 1





#LIST() COMSTUCTER

thislist=list(('apple','banana','cherry'))
print(thislist)








num=input('enter the num:')
print(num[::-1])




    






