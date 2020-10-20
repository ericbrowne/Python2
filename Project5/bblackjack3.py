# Eric Browne Student ID: 873517924
#Blackjack3, Project 5
#Python 2: Software Development

'''For this project, we are adding onto the previous assignment of the blackjack simulations:'''


import random
import sys
from collections import namedtuple
import csv
import datetime

Score = namedtuple("Score","total soft_ace_count")
Stand = namedtuple("Stand","stand total")

class Hand:
    "The Hand class represents a single 'hand' in blackjack"



    def add_card(self):
         card = random.randint(1,13)
         self.cards.append(card)
         (self.total, self.soft_ace_count) = self.score()

    def __init__(self,cards):
        self.cards = cards if cards != None else []
        (self.total, self.soft_ace_count) = self.score()

    def __str__(self):
        return self.cards.__str__()+ " " +str(self.total) + "/"+ str(self.soft_ace_count)

    def is_blackjack(self):
        return len(self.cards) == 2 and self.card[0] >= 10 and self.cards[1] ==1

    def is_bust(self):
        return self.total > 21

    def score(self):
        '''This returns a tuple with the score and number of aces remaining '''

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
    '''This class is all relating to the process of 'standing', and playing a hand:'''
    def __init__(self,stand_on_value,stand_on_soft):
        self.stand_on_value = stand_on_value
        self.stand_on_soft = stand_on_soft

    def __repr__(self):
        return "Strategy: Stand on " + str(self.stand_on_value)+ " " + ("soft" if self.stand_on_soft else "Hard")

    def __str__(self):
        return  ("S" if self.stand_on_soft else "H") + " " + str(self.stand_on_value)

    def stand(self, hand):
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
    	This function represents the logic behind playing a single hand of blackjack, and returns the final score.  If
        the score is greater than or equal to 22, it returns value 22, otherwise, returns the actual final total of the hand."""
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

def sim_game(player_strat, dealer_strat):
    """This function will compare the dealer's strategy with player's strategy; and determines who wins"""
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
    This will produce every possible strategy and output them to a CSV file.
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
