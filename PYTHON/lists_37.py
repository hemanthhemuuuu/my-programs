#MATCH-CASE STATEMENT (SWITCH)--ELIF STATEMETS USING AS CASE:

##EXAMOLE----2

def week(day):
    match day:
        case "sunday" | 'Saturday':
            return True

print(week("sunday"))

###EXAMPLE---1

def day(dayy):
   
    match dayy:
         case 1:
            return 'Sunday'
         case 2:
            return 'Monday'
         case 3:
            return 'Tuesday'
         case 4:
            return 'Wednesday'
        
         case 5:
            return 'Thursday'
         case 6:
            return 'Friday'
         case 7:
            return 'Saturday'
         
dayyy=day(int(input('enter dayy:')))
print(dayyy)



#LISTS COMPHREHENSION -- WAY TO CREATE  A LISTS

#SYNTAX--[EXP FOR VALUE IN RANGE IF CONDITION]

#CONDITIONS--[EXP FOR VALUE IN RANGE IF CONDITION]

num=[1,2,3,-4,-5,-6]
pos=[x for x in num if x > 0]
neg=[x for x in num if x < 0]
even=[x for x in num if x%2==0]
print(even)







#LISTS

f=['ad','bs','cs','ds']
f=[x[0] for x in f]
print(f)



d=[2*x for x in range(10,21)]
s=[y*y for y in range(10,21)]
print(s)



#EX--1


l=[]

for x in range(1,11):
     l.append(x *2)

print(l) 

