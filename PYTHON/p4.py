




#NESTED LOOP--A LOOP INSIDE THE OTHER LOOP
#OUTER LOOP
#INNER LOOP

rows=int(input('enter the rows:'))
col=int(input('enter the col:'))
sym=input('enetr the symbol:')

for x in range(rows):
        for y in range(col):
           print(sym,end="")
        print()






for x in range (3):
    for y in range(1,10):
        print(y,end=" ")
    print("")






# COUNTDOWN TIMER PROGRAM

import time 

t = int(input('Enter the time in seconds: '))

for x in range(t, 0, -1):  
    sec = x % 60
    min = int(x /60) % 60
    hrs = int(x / 3600) % 24
    print(f'{hrs:02}:{min:02}:{sec:02}')
    time.sleep(1)

print('TIME UP!')
