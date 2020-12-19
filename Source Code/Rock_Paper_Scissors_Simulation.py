# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:52:40 2019
Modified on Fri Dec 04 2020
@author: asithu
"""

def game():
    choices=['rock','paper','scissors']
    player1=input("Please enter your choice:")
    if player1.lower() not in choices:
        player1=input("Please enter a valid choice:")
    player2=choices[random.randint(0,2)]
    win=0
    n=int(input("Enter the number of rounds to be simulated:")) # simulate for n rounds
    for i in range(n):
        player2=choices[random.randint(0,2)]
        if player1.lower()==player2:
            print('It\'s a draw')
        elif player1.lower()=='rock':
            if player2=='scissors':
                print("You win. rock wins over scissors")
                win+=1
            else:
              print("You lose. paper wins over rock")
        elif player1.lower()=='scissors':
            if player2=='paper':
                print("You win. scissors wins over paper")
                win+=1
            else:
              print("You lose. rock wins over scissors")
        elif player1.lower()=='paper':
            if player2=='scissors':
                print("You lose. scissors wins over paper")
            else:
              print("You win. paper wins over rock")
              win+=1
    win_perc=round(win/n,3)
    print("Win% on choosing",player1.lower(),"in",n,"rounds is:",win_perc*100)
    check = input("Up for another round?(Y/N):")
    if check.lower()=="y":
        game()
    else:
        print("Thanks for playing")

import random
print("Let's check win% in a few games of Rock, Paper and Scissors with one specific choice")
game()



