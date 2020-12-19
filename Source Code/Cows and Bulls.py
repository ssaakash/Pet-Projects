# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:28:14 2019
Modified on Fri Dec 04 2020
@author: asithu
"""
import random

def game():
    num=random.randint(1000,9999)
    user_num=int(input("Let\'s play a game of cows and bulls.\nCows refer to correct digits\nBulls refer to incorrect digits\nGuess the 4 digit number:" ))
    while user_num>9999 or user_num<1000:
        user_num=int(input("The guess should be a 4 digit number:" ))
    cows=0
    bulls=0
    count=1
    while cows<4:
        if count>1:
           user_num=int(input("Guess again:")) 
        cows=0
        bulls=0
        a=user_num//(10**3)==num//(10**3) # thousands digit
        b=((user_num%(10**3))//100)==((num%(10**3))//100) # hundreds digit
        c=((user_num%(10**3))%100)//10==((num%(10**3))%100)//10 # tens digit
        d=((user_num%(10**3))%100)%10==((num%(10**3))%100)%10 # ones digit
        if a:
            cows+=1
        else:
            bulls+=1
        if b:
            cows+=1
        else:
            bulls+=1
        if c:
            cows+=1
        else:
            bulls+=1
        if d:
            cows+=1
        else:
            bulls+=1
        print("No. of cows:{} \nNo. of bulls:{}".format(cows,bulls))
        count+=1
    print("Bravo! You guessed the number {} in {} turns".format(num,count))
    check=input("Up for another round? (Y/N):")
    if check.lower()=='y':
        game()
        
        
game()