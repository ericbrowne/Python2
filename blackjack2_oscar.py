# ==============================
# NAME: Oscar Pachon
# DATE: 2/06/2020
# CLASS: COMP 3006-2
# HOMEWORK NUMBER: Assignment 4
"""
Overview :
Enhanced code from Week 3’s assignment that calculates totals hans for all possible Blackjack strategies.
This program is based out of the program from assignment #3 given by the instructor.
"""

import random
import sys
from collections import namedtuple
import csv
import datetime

Score = namedtuple("Score","total soft_ace_count")
Stand = namedtuple("Stand","stand total")


def get_card():
    '''Returns a random value from 1 to 13 to represent a card value.
    1 = ace, 2–10 number cards, {11,12,13} are jack, queen, king.
    '''
    return random.randint(1,13)

def score(cards):
    '''Returns a tuple representing the score of the hand and the number of
    remaining soft aces.
    '''

    ## sort so we can add the total of the aces last
    cards.sort(reverse = True)

    soft_ace_count = 0
    total = 0

    for card in cards:
        if card >= 10:
            total += 10
        elif card > 1:
            total += card
        elif total <= 10:
            total += 11
            soft_ace_count += 1
        else:
            total += 1

    return Score(total, soft_ace_count)

def stand(stand_on_value, stand_on_soft, cards):
    '''Returns a Boolean indicating whether the player will stand with the
    given cards according to the specified strategy.
    '''
    total, soft_ace_count = score(cards)

    ## always hit if the score is below the stand value
    if total < stand_on_value:
        return Stand(False,total)

    ## always stand if the score is above the stand value
    if total > stand_on_value:
        return Stand(True,total)

    ## stand on the stand value only if no soft aces or playing the hard strategy
    if soft_ace_count == 0 or stand_on_soft:
        return Stand(True,total)

    return Stand(False,total)

def play_hand(stand_on_value, stand_on_soft):
	"""
	This function encapsulates the logic of playing a single hand and returns
	the final score. If the score is 22 or greater (i.e., bust),it returns the
	value 22; otherwise, return the actual final total of the hand.
	"""

	total = 0
	cards = []

	while True:
		(stay,total) = stand(stand_on_value, stand_on_soft, cards)

		if total > 21:
			return 22

		if stay:
			break

		cards.append(get_card())

	return total

"""
def old_main():
    '''Runs the specified number of blackjack simulations using the specified
    strategy and prints out the percentage of time the hand busted.
    Usage: blackjack.py <num-simulations> <stand-on-value (1-20)> <'soft'|'hard'>
    '''
    args = sys.argv[1:]

    #print(stand(17, False, [1,6,10]))   #clean
    print(play_hand(17, False))
    return                          #clean

    if len(args) != 3:
        print(main.__doc__, file = sys.stderr)
        raise TypeError

    num_simulations = int(args[0])
    stand_on_value = int(args[1])

    if(num_simulations < 1):
        raise ValueError(f'Invalid number of simulations: {num_simulations}. num_simulations must be positive.')

    if(stand_on_value > 20 or stand_on_value < 1):
        raise ValueError(f'Invalid stand on value: {stand_on_value}. Value values are 1-20.')

    if(args[2] != 'soft' and args[2] != 'hard'):
        print(main.__doc__, file = sys.stderr)
        raise ValueError(f'Unknown argument: {args[2]}')

    stand_on_soft = args[2] == 'soft'
    bust_count = 0

    for i in range(0, num_simulations):
        cards = [get_card(), get_card()]

        while not stand(stand_on_value, stand_on_soft, cards):
            cards.append(get_card())
            new_score = score(cards)
            bust_count += new_score[0] > 21

    print(bust_count/num_simulations)
"""

def main():
    """
    Expected a single argument, and run all of the strategies that many time. then
    build a table with results and write the table to a csv file.

    """
    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage requires a single argument: number of simulations to run")
    #receving the argument
    num_sims = int(args[0])
    #preparing the data for the table
    data = {}
    for i in range(13,21):
        data["H"+str(i)] = [0,0,0,0,0,0,0,0,0,0]
        data["S"+str(i)] = [0,0,0,0,0,0,0,0,0,0]

    #generating the data

    for i in range(13,21):
        hardkey = "H" + str(i)
        softkey = "S" + str(i)

        for k in range (0, num_sims):
            hardVal = play_hand(i, False)
            softVal = play_hand(i, True)

            hardIndex = hardVal - 13
            softIndex = softVal - 13

            data[hardkey][hardIndex] += 1
            data[softkey][softIndex] += 1

    #get current time in milliseconds
    ticks = int(datetime.datetime.utcnow().timestamp()*1000)

    #creating csv file

    with open("blackjack-"+str(ticks)+".csv","w") as csvfile:
        writer = csv.writer(csvfile, delimiter = " ",
            quotechar ="|",quoting = csv.QUOTE_MINIMAL)
        writer.writerow(["Strategy","13","14","15","16","17","18","19","20","21","Bust"])

        for i in range(13,21):
            writer.writerow(["H"+str(i)] + data["H"+str(i)])
            writer.writerow(["S"+str(i)] + data["S"+str(i)])

if __name__ == '__main__':
    main()
