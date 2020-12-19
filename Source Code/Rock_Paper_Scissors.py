# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:52:40 2019
Modified on Fri Dec 04 2020
@author: asithu
"""
def game(choices):
    player1=input("Please enter your choice:")
    while player1.lower() not in choices:
        player1=input("Please enter a valid choice:")
    player2=choices[random.randint(0,2)]    
    if player1.lower()==player2:
        print('It\'s a draw')
    elif player1.lower()=='rock':
        if player2=='scissors':
            print("You win. rock wins over scissors")
        else:
          print("You lose. paper wins over rock") 
    elif player1.lower()=='scissors':
        if player2=='paper':
            print("You win. scissors wins over paper")
        else:
          print("You lose. rock wins over scissors")
    elif player1.lower()=='paper':
        if player2=='scissors':
            print("You lose. scissors wins over paper")
        else:
          print("You win. paper wins over rock")
    check=input("Up for another round? (Y/N):")
    if check.lower()=='y':
        game(choices)



import random
choices=['rock','paper','scissors']
print("Let's play a game of Rock, Paper and Scissors")
game(choices)     
print("Thanks for playing, See you later")




    