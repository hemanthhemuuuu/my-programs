

#DICE ROLLER PROGRAM

import random

#● ┌ ─ ┐ │ └ ┘

 "┌─────────┐"
 "│         │"











#ROCK , SCISSORS AND PAPER GAME

import random

op=('rock','scissors','paper')
run=True

while True:
           plr=0
           com=random.choice(op)
           while plr not in op:
             plr=input('enter the ch(rock,scissors ,paper):')
             print(f'player :{plr}')
             print(f'computer:{com}')
             if plr==com:
                 print('Tie!')
             if plr=='rock' and com=='scissor':
                 print('YOU WON!')
             elif plr=='scissor' and com=='paper':
                 print('YOU WON!')
             elif plr=='paper' and com=='rock':
                 print('YOU WON!')
             else:
                print('YOU LOST!')
                
               
             put=input('enter op (y/n):').lower()
             if not put=='y':
                run=False

print('THANK YOU FOR  PLAYING')





#PYTHON NUMBER GUESSING GAME

import random

low=1
high=100
ans=random.randint(low,high)
guesses=0
is_run=True

print('!!!!PYTHON NUMBER GUESS WELCOMES YOU!!!!')
print(f'enter num {low} between {high}')

while is_run:
    guess=input("enter the num:")
    print(f'the random num is {ans}')

    if guess.isdigit():
       guess=int(guess)
       guesses +=1
  

       if guess<low or guess>high:
           print('that num is outoff range!')
           print(f'enter num {low} between {high}')
       elif guess<ans:
           print('Too low!Try Again!')
       elif guess>ans:
           print('Too High!Try Again!')
       else:
           print(f'CORRECT! the answer was {ans}')
           print(f'number of guesses are {guesses}')
           is_run=False
    else:
       print('INVALID GUESS!')
       print(f'PLEASE enter num {low} between {high}')







#RANDOM NUMBERS

import random
cards=['1','2','3','4','5','6','Q','K']
random.shuffle(cards)
print(cards)


#ROCK PAPER SCISSORS BY TUPLE IN RANDOM NUMBERS

#op=('rock','paper','scissors')
#ch=random.choice(op)
#print(c)



#num=random.randint(low,high)
low=1
high=100
num=random.random()
print(num)


#print(help(random))
