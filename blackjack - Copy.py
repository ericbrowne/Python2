# Eric Browne Student ID#: 873917524
#This selects a random number between 1 and 13

import random
import math
import sys

def get_card():
    '''This function will return a random number between 1 and 13'''
    return random.randint(1,13)

def score(cards):
    '''This function will calculate the score in a given black jack hand
    by calling the get_card function'''
    total_list = [] #intialize a list
    for i in cards:
        total_list.append(i)
    soft_ace_count = 0 #intialize the amount of soft aces left over
    total = 0 #intialize the total
    for i in range(0,len(total_list)):  #Change the face cards to be value = 10, aces = 11
        if total_list[i] > 10: #face cards
            total_list[i] = 10
        if total_list[i] == 1: #ace
            total_list[i] = 11
    for i in range(0,len(total_list)):  #first initially add up the value
        total += total_list[i]

    if total > 21: #a bust
        for i in range(0,len(total_list)): #any aces in ur hand to switch to 1?
            if total>21:
                if total_list[i] == 11:
                    total_list[i] = 1
                    total=total-10
        for num in total_list:
            if num == 11:
                soft_ace_count += 1
    else:
        for num in total_list:
            if num == 11:
                soft_ace_count += 1
    return (total,soft_ace_count)


def stand(stand_on_value,stand_on_soft,cards):
    '''This function will determine if a player wants to stand
    or hit in a given blackjack hand'''
    total, soft_ace_count = score(cards)
    stand = True
    if total> stand_on_value:
        stand = True #Stand!, dont hit again
    elif total < stand_on_value:
        stand = False #we want to hit
    else: #the total equals the stand on value
        if soft_ace_count > 0:  #we have at least soft ace
            if stand_on_soft == True:
                stand = True #stand, because we dont care even tho we have a soft ace
            if stand_on_soft == False:
                stand = False #we want to hit, because we arent going to stand
        else:  #no soft aces, but total = stand value
            if stand_on_soft == True:
                stand = True #stand!
            if stand_on_soft == False:
                stand = False #hit!
    return stand

# Oh boy here we go
def main():
    '''This main function will run through a certain number
    of simulations and give back the percentage of busting in a
    black jack hand'''
    stand_on_soft = True
    #initialize some flags
    num_simluation_flag = int(sys.argv[1])
    stand_on_value_flag = int(sys.argv[2])
    sofhar_flag = str(sys.argv[3])

    #validation:
    if num_simluation_flag < 0 :
        raise ValueError
    if stand_on_value_flag < 1 or stand_on_value_flag > 20:
        raise ValueError
    if sofhar_flag != "hard" and sofhar_flag != "soft":
        raise ValueError
    if sofhar_flag == 'soft':
        stand_on_soft = False
    bustcount = 0
    for i in range(num_simluation_flag):
        cards = [get_card(),get_card()]
        boolean = stand(stand_on_value_flag,stand_on_soft,cards)
        while not boolean:   #if we are not standing, then we are hitting
            cards.append(get_card()) #hit!
            boolean = stand(stand_on_value_flag,stand_on_soft,cards) #new hand, so do we stand or hit?
        #if we are finally staying, and no more hitting, then calculate the score
        finalscore = score(cards)
        if finalscore[0]>21:
            bustcount += 1

    #outside the loop:
    final_percentage = (bustcount/num_simluation_flag)*100
    return final_percentage

if __name__=="__main__":
    print(main())
