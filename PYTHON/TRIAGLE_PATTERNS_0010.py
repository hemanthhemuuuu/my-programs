#PRINTING THE NUMBERS AS AN TRANGLES









#SHORT METHOD FOR SOTING AND MERGING

l1 = [1, 3, 5, 6]
l2 = [2, 4, 6, 8]

res=sorted(l1+l2)
print(res)




#MERGE AND SORT OF 2 LISTS
l1 = [1, 3, 5, 6]
l2 = [2, 4, 6, 8]
res = []
i = j = 0

while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        res.append(l1[i])
        i += 1
    else:
        res.append(l2[j])
        j += 1

# Append remaining elements
res.extend(l1[i:])
res.extend(l2[j:])

print(res)







#PRODUCT OF THE DIGITS OF NUMBER

n=int(input('enetr num:'))
t=1
while n!=0:
    d=n%10
    t=t*d
    n=n//10

print(t)





#SUM OF THE DIGITS OF A NUMBER

n=int(input("enter num:"))
total=0
while n!=0:
      digit=n%10
      total=total+digit
      n=n//10
  
print(total)




#REVERSE RHOMBUS PATTERN

r=8

for i in range(r-1,0,-1):
    for j in range(r-i-1):
        print(' ',end="")
    for j in range(2*r):
        print("*",end='')
    print()





#RHOMBUS PATTERN
r=6
for i in range(r):
    for j in range(r-i-1):
        print(' ',end="")
    for j in range(2*6):
        print('*',end='')
    print()






#REVERSE TRIANGLE PATTERN

r=6
for i in range(r-1,-1,-1):
    for j in range(r-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print('*',end="")
    print('')







#TRIANGLE PATTERNS IN PYTHON

rows=6

for i in range(rows):
          for j in range(rows-i-1):
              print(" ",end="")
          for j in range(2*i+1):
              print('*',end="")
          print()
