



#DICTIONARY---COLLECTION OF {KEY:VALUE} PAIRS
#ORDERED , CHANGABLE AND DULICATES OOK


#CONCESSION STAND PROGRAM USING DICTIONARY METHOD

print('------MENU-----')
menu={"chips":2.00,
      "pizza":3.00,
      "soda":4.00,
      "fries":5.00,}




cart=[]
total=0
for key,keys in menu.items():
    print(f'{key:10}:${keys:.2f}')

while True:
    food=input('entre the items(q to quit):').lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
       

print('-----YOUR ORDER-----')

for food in cart:

    print(food,end=' ')
    print()

total +=menu.get(food)
print(f'total is:{total:.2f}')


print('--------THANK YOU DEAR-------')


#values=menu.values()
#print(values)    








cap={"USA" : "WASH",
     "INDIA" : "NEW DELHI",
     "RUSSIA" : "MOSCOW",
     "AP" : "AMARAVATHI"}

for x in cap.values():
    print(x)

#print(dir(cap))   TO KNOW THW ATTRIBUTES nd IDEA TO SOLVE MORE ON THIS CONCEPTS
#print(help(cap))

#print(cap.get("INDIA"))


#cap.update({"germany": "berlin"})
#cap.pop("USA")
#cap.popitem()
#cap.clear()


#item=cap.items()

for key,val in cap.items():
          print(f"{key}:{val}")                #item prints a dictionary object which resembles a 2-D list of tupples





#val=cap.values()

#for val in cap.values():
#         print(val)








#keys=cap.keys()

#for x in cap.keys():
#     print(x)
        
for x in cap:
    print(x)


if cap.get("INDIA"):
    print("this is a capital")
else:
    print("this is not a capital")























#PYTHON QUIZ  GAME using tupple
# Questions
que = ("what?",
       "when?",
       "where?",
       "why?",
       "how?")

# Options for each question
op = (("A.1", "B.2", "C.3", "D.4"),
      ("A.1", "B.2", "C.3", "D.4"),
      ("A.1", "B.2", "C.3", "D.4"),
      ("A.1", "B.2", "C.3", "D.4"),
      ("A.1", "B.2", "C.3", "D.4"))

# Correct answers
ans = ("A", "B", "C", "D", "A")

# Score and tracking
score = 0
guesses = []
que_num = 0

for x in que:
    print("-----------")
    print(x)
    for y in op[que_num]:
        print(y)

    guess = input("Enter an option (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == ans[que_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"{ans[que_num]} is the correct answer.")

    que_num += 1

# Final result
print("\nYour guesses:", guesses)
print("Correct answers:", ans)
print(f"Your score: {score}/{len(que)}")





#NUM PAD USING TUPPLE WHICH IS ORDERED, UNCHANGE AND NOO DUPLICATES

num=((1,2,3),
     (4,5,6),
     (7,8,9),
     ("*",0,"#"))

for x in num:
    for y in x:
        print(y,end="   ")
    print()










#2-DIMENSTION LISTS,SETS AND TUPPLES
f = ['apple', 'banana', 'coconut', 'dragon']
veg = ['brinjal', 'benda', 'ladys', 'koora']
gro = ['chik', 'mutton', 'fish', 'crab']

t = [f, veg, gro]

for category in t:
    for item in category:
        print(item, end=" ")
    print()  # for new line between categories


#t=[f]
#print(t,veg,gro)    for indivisual ones :print([1][1])==brinjal












#SHOPPPING CART PROGRAM

foods=[]
prices=[]
total=0

while True:
    food=input('enter a food to buy(or "q" to quit) :')
    if food.lower()=="q":
        break
    else:
        price=float(input(f"enter the prices a {food}:"))
        foods.append(food)
        prices.append(price)


print("- - - - YOUR CART- - - - ")

for food in foods:
    print(food,end=" ")

for price in prices:
    total +=price

    print(f"your total is :{total}")











#COLLECTION--ONE VARIABLE STORES THE MULTIPLE VALUES

#LISTS--[] ORDERED AND CHANGABLE ,DUPLICATES OK

f=('apple','banana','coconut','dragon')

#fruits.app("pineapple")
#fruits.remove("dragon")
#fruits.sort()
#print(fruits.reverse())
#fruits.insert(0,"guava")
#fruits.clear()
#fruits.pop(-1)


#SET
#f.add("pineapple")
f.remove("banana")
print(f)



#print(f[0])                            #indexind operator 
#print("apple" in f)
#print(len(f))

#print(dir(f))  show s the methods
#print(help(f))   descriptions about the methods and attributes 



#print(f)
#for x in f:
 #   print(x)

