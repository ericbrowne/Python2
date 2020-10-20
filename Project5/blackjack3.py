# Eric Browne Student ID: 873517924
#Blackjack3, Project 5
#Python 2: Software Development

import random
import sys
from collections import namedtuple
import csv
import datetime

Score = namedtuple("Score","total soft_ace_count")
Stand = namedtuple("Stand","stand total")

class Hand:
    """encapsulates some of the logic developed in the previous two assignments. The Hand class represents a single hand of blackjack """

    def __init__(self,cards):
        self.cards = cards if cards != None else []
        (self.total, self.soft_ace_count) = self.score()

    def __str__(self):
        return self.cards.__str__()+ " " +str(self.total) + "/"+ str(self.soft_ace_count)

    def add_card(self):
         card = random.randint(1,13)
         self.cards.append(card)
         (self.total, self.soft_ace_count) = self.score()

    def is_blackjack(self):
        return len(self.cards) == 2 and self.card[0] >= 10 and self.cards[1] ==1

    def is_bust(self):
        return self.total > 21

    def score(self):
        '''Returns a tuple representing the score of the hand and the number of
        remaining soft aces.
        '''

        ## sort so we can add the total of the aces last
        self.cards.sort(reverse = True)

        soft_ace_count = 0
        total = 0

        for card in self.cards:
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

class Strategy:
    """This class will encapsulate the logic from the previous assignments related to standing and playing a hand. """
    def __init__(self,stand_on_value,stand_on_soft):
        self.stand_on_value = stand_on_value
        self.stand_on_soft = stand_on_soft

    def __repr__(self):
        return "Strategy: Stand on " + str(self.stand_on_value)+ " " + ("soft" if self.stand_on_soft else "Hard")

    def __str__(self):
        return  ("S" if self.stand_on_soft else "H") + " " + str(self.stand_on_value)

    def stand(self, hand):
        '''Returns a Boolean indicating whether the player will stand with the
        given cards according to the specified strategy.
        '''

        ## always hit if the score is below the stand value
        if hand.total < self.stand_on_value:
            return Stand(False,hand.total)

        ## always stand if the score is above the stand value
        if hand.total > self.stand_on_value:
            return Stand(True,hand.total)

        ## stand on the stand value only if no soft aces or playing the hard strategy
        if hand.soft_ace_count == 0 or self.stand_on_soft:
            return Stand(True,hand.total)

        return Stand(False,hand.total)

    def play(self):
    	"""
    	This function encapsulates the logic of playing a single hand and returns
    	the final score. If the score is 22 or greater (i.e., bust),it returns the
    	value 22; otherwise, return the actual final total of the hand.
    	"""
    	total = 0
    	hand = Hand([])

    	while True:
    		(stay,total) = self.stand(hand)

    		if total > 21:
    			return 22

    		if stay:
    			break

    		hand.add_card()

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
def sim_game(player_strat, dealer_strat):
    """compares dealer strategy with player strategy based on the rules of the game and decides who wins"""
    ptotal = player_strat.play()
    if ptotal > 21:
        return False
    dtotal = dealer_strat.play()
    if dtotal > 21:
        return True
    if dtotal == ptotal:
        return False
    return ptotal > dtotal

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
        data["H"+str(i)] = {}
        data["S"+str(i)] = {}
        for k in range(13,21):
            data["H"+str(i)]["H"+str(k)] = 0
            data["H"+str(i)]["S"+str(k)] = 0

            data["S"+str(i)]["H"+str(k)] = 0
            data["S"+str(i)]["S"+str(k)] = 0


    #generating the data

    for i in range(13,21):
        phardkey = "H" + str(i)
        psoftkey = "S" + str(i)
        phardstrat = Strategy(i, False)
        psoftstrat = Strategy(i, True)

        for k in range(13, 21):
            dhardkey = "H" + str(k)
            dsoftkey = "S" + str(k)
            dhardstrat = Strategy(k, False)
            dsoftstrat = Strategy(k, True)

            for j in range (0, num_sims):
                hvsh = sim_game(phardstrat, dhardstrat)
                hvss = sim_game(phardstrat, dsoftstrat)
                svsh = sim_game(psoftstrat, dhardstrat)
                svss = sim_game(psoftstrat, dsoftstrat)


                data[phardkey][dhardkey] += 1 if hvsh else 0
                data[phardkey][dsoftkey] += 1 if hvss else 0
                data[psoftkey][dhardkey] += 1 if svsh else 0
                data[psoftkey][dsoftkey] += 1 if svss else 0


    #get current time in milliseconds
    ticks = int(datetime.datetime.utcnow().timestamp()*1000)

    #creating csv file

    with open("blackjack3-"+str(ticks)+".csv","w") as csvfile:
        writer = csv.writer(csvfile, delimiter = " ",
            quotechar ="|",quoting = csv.QUOTE_MINIMAL)

        header = ["P-Strategy"]
        for k in range(13,21):
            header.append("D-H" + str(k))
            header.append("D-S" + str(k))

        writer.writerow(header)

        for i in range(13,21):
            hrow = ["P-H"+str(i)]
            srow = ["P-S"+str(i)]

            for k in range(13,21):
                hrow.append(data["H"+str(i)]["H"+str(k)])
                hrow.append(data["H"+str(i)]["S"+str(k)])
                srow.append(data["S"+str(i)]["H"+str(k)])
                srow.append(data["S"+str(i)]["S"+str(k)])

            writer.writerow(hrow)
            writer.writerow(srow)

if __name__ == '__main__':
    main()
