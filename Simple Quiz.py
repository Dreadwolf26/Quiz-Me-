# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:22:40 2022

@author: chris
"""

#Quiz Game 
print('Welcome to my computer quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
        quit()
         
print('OK! Lets play :)')
score = 0

answer= input("What does CPU stand for? ")
if answer.lower() == 'central processing unit': 
      print('Correct!')
      score += 1
else:
    print('Incorrect!')
    print('Try Again!')    

answer= input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit': 
        print('Correct!')
        score += 1
else:
    print('Incorrect!')
    print('Try Again!')    

answer= input("What does RAM stand for? ")
if answer == 'random access memory': 
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('Try Again!')     
  

      #line 46 score/4 will have to be updated if number of questions are changed.   
print('You got ' + str(score) +' questions correct!')
print('You got ' + str((score/4) * 100) +' %')
                