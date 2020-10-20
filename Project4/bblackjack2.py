# Eric Browne StudentID#: 873517924
import random
import sys
from collections import namedtuple
import csv
import datetime

Score = namedtuple("Score","total soft_ace_count")
Stand = namedtuple("Stand","stand total")


def get_card():
    '''This simulates the act of getting a card, random number between 1 and 13
    '''
    return random.randint(1,13)

def score(cards):
    '''Returns a tuple representing the score of the hand and the number of
    remaining soft aces.   '''

    #sort so we can add the total of the aces last
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

    #Hit if score < stand value
    if total < stand_on_value:
        return Stand(False,total)

    #stand is score > stand value
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



def main():
    """
    The output of this will run to a csv file containing the number of busts
    for each soft/hard strategy
    """
    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage requires a single argument: number of simulations to run")
    #receving the argument
    number_simulations = int(args[0])
    #preparing the data for the table
    data = {}
    for i in range(13,21):
        data["H"+str(i)] = [0,0,0,0,0,0,0,0,0,0]
        data["S"+str(i)] = [0,0,0,0,0,0,0,0,0,0]

    #Now generate the data to be written to a csv file:
    for i in range(13,21):
        hardkey = "H" + str(i)
        softkey = "S" + str(i)

        for k in range (0, number_simulations):
            hardVal = play_hand(i, False)
            softVal = play_hand(i, True)

            hardIndex = hardVal - 13
            softIndex = softVal - 13

            data[hardkey][hardIndex] += 1
            data[softkey][softIndex] += 1

    #Now, we must get the current time in milliseconds
    ticks = int(datetime.datetime.utcnow().timestamp()*1000)

    #Now we need to write this to a CSV file:
    with open("blackjack-"+str(ticks)+".csv","w") as csvfile:
        writer = csv.writer(csvfile, delimiter = " ", quotechar ="|",quoting = csv.QUOTE_MINIMAL)
        writer.writerow(["Strategy","13","14","15","16","17","18","19","20","21","Bust"])

        for i in range(13,21):
            writer.writerow(["S"+str(i)] + data["S"+str(i)])

            writer.writerow(["H"+str(i)] + data["H"+str(i)])

if __name__ == '__main__':
    main()
