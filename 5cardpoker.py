#!/usr/bin/env python2

#  First attempt at writing a 5 card draw poker game

import random

cards = ["As", "Ac", "Ah", "Ad","Ks", "Kc", "Kh", "Kd","Qs", "Qc", "Qh", "Qd","Js", "Jc", "Jh", "Jd","10s", "10c", "10h", "10d",
         "9s", "9c", "9h", "9d","8s", "8c", "8h", "8d","7s", "7c", "7h", "7d","6s", "6c", "6h", "6d","5s", "5c", "5h", "5d","4s",
         "4c", "4h", "4d","3s", "3c", "3h", "3d","2s", "2c", "2h", "2d"]
hands = ["high card", "pair", "two pair", "three of a kind", "strait", "flush", "full house", "four of a kind", "strait flush", "royal flush"]
facecard = {"A": 14, "K": 13, "Q": 12, "J": 11}
cardface = {14: "A", 13: "K", 12: "Q", 11: "J"}

players = []
player0 = []
player1 = []
player2 = []
player3 = []
player4 = []

def player_name(x):
    player = raw_input("What is player %s's name? " % str(x+1) )
    players.append(player)

def pick_players():
    strPlayers = raw_input("How many players (up to five)? ")
    if len(strPlayers) > 1:
        print "%s is an invalid entry, please try again" % strPlayers
        start()
    numPlayers = int(strPlayers)
    print
    if numPlayers in (2, 3, 4, 5):
        for x in range(0,numPlayers):
            player_name(x)
            print "Player %s added" % players[x]
    else:
        print "You must choose 2 to 5 players to play draw poker"
        print "Please try again"
        start()

##def playagain():
##    print
##    replay = raw_input("Do you want to play again Y/N")
##    if replay in ("Y", "y", "YES", "Yes"):
##        sameplayers = raw_input("Same Players Y/N")
##        if sameplayers in ("Y", "y", "YES", "Yes"):
##            game()
##        else:
##            start()
##    else:
##        pass


def ranks(hand):
    count = 0
    numRange = 0
    spades = 0
    hearts = 0
    clubs = 0
    diamonds = 0
    strait = 0
    flush = 0
    three = 0
    pair1 = 0
    pair2 = 0
    likecards = 1
    numPair = []
    
##-------------- Uncomment for testing ---------------    
##    test = ["As","10s","Js","Qs","Ks"]
##    for x in test:
##----------------------------------------------------        
    for x in hand:
        card = x
        if len(card) == 3:
            cardN = card[0:2]
            cardT = card[2]
        else:
            cardN = card[0]
            cardT = card[1]

        if cardN in ("A", "K", "Q", "J"):
            cardN = facecard[cardN]
        else:
            cardN = int(cardN)

        count += cardN
            
        numPair.append(cardN)
        
        if cardT == 's':
            spades += 1
        elif cardT == 'h':
            hearts += 1
        elif cardT == 'c':
            clubs += 1
        elif cardT == 'd':
            diamonds += 1

        if spades == 5:
            flush = 1
            suit = 'spades'
        elif  hearts == 5:
            flush = 1
            suit = 'hearts'
        elif clubs == 5:
            flush = 1
            suit = 'clubs'
        elif diamonds == 5:
            flush = 1
            suit = 'diamonds'
        else:
            flush = 0
            
    numPair.sort()
    for r in xrange(0, len(numPair)-1):
        if numPair[r+1] - numPair[r] != 1:
            strait = 0
        else:
            strait += 1
                   

        if numPair[r+1] == numPair[r]:
            likecards += 1
            if likecards == 3:
                three = str(numPair[r])
                pair2 = numPair[4]
                likecards = 5
                break
            if pair1 == 0:
                pair1 = numPair[r]
            else:
                pair2 = numPair[r]
                
    if strait == 4:
        if numPair[4] - numPair[3] == 1:
            strait += 1
        
    for a in range(0,5):
        if numPair[a] > 10:
            numPair[a] = cardface[numPair[a]]
        else:
            numPair[a] = str(numPair[a])

    if pair1 > 10:
        pair1 = cardface[pair1]
    else:
        pair1 = str(pair1)
        
    if pair2 > 10:
        pair2 = cardface[pair2]
    else:
        pair2 = str(pair2)
            

    if flush == 1 and strait == 5 and count == 60:
        outcome = '*** Royal Flush  ***({})'.format(suit)
    elif flush == 1 and strait == 5:
        outcome = 'Strait Flush to the {}'.format(numPair[4])
    elif pair1 == pair2 and likecards == 4:
        outcome = 'Four of a kind ({}\'s)'.format(pair1)
    elif likecards == 5:
        if three == pair1:
            outcome = 'Full House ({}\'s full of {}\'s)'.format(pair2, three)
        else:
            outcome = 'Full House ({}\'s full of {}\'s)'.format(pair1, three)
    elif flush == 1:
        outcome = 'Flush ({})'.format(suit)
    elif strait == 5:
        outcome = 'Strait to the {}'.format(numPair[4])
    elif likecards == 3:
        outcome = 'Three of a kind ({}\'s)'.format(pair1)
    elif likecards == 4 and pair1 != pair2:
        outcome = 'Two pair ({}\'s and {}\'s)'.format(pair1, pair2)
    elif likecards == 2 and pair1 != '0':
        outcome = 'One pair ({}\'s)'.format(pair1)
    elif likecards < 2:
        outcome = 'High Card ({})' .format(numPair[4])
    else:
        outcome = 'An Error has occurred'

    return outcome

def game():
    n = len(players)
    for x in range(0,5):
        if n == 5:
            player0.append(cards.pop(random.randint(0, len(cards) - 1)))
            player1.append(cards.pop(random.randint(0, len(cards) - 1)))
            player2.append(cards.pop(random.randint(0, len(cards) - 1)))
            player3.append(cards.pop(random.randint(0, len(cards) - 1)))
            player4.append(cards.pop(random.randint(0, len(cards) - 1)))
        elif n == 4:
            player0.append(cards.pop(random.randint(0, len(cards) - 1)))
            player1.append(cards.pop(random.randint(0, len(cards) - 1)))
            player2.append(cards.pop(random.randint(0, len(cards) - 1)))
            player3.append(cards.pop(random.randint(0, len(cards) - 1)))
        elif n == 3:
            player0.append(cards.pop(random.randint(0, len(cards) - 1)))
            player1.append(cards.pop(random.randint(0, len(cards) - 1)))
            player2.append(cards.pop(random.randint(0, len(cards) - 1)))
        elif n == 2:
            player0.append(cards.pop(random.randint(0, len(cards) - 1)))
            player1.append(cards.pop(random.randint(0, len(cards) - 1)))
        
    hand0 = ranks(player0)
    myHand = player0[0] + " " + player0[1] + " " + player0[2] + " " + player0[3] + " " + player0[4]
    print "%s\'s hand is:" % (players[0])
    print "       " + (myHand) + ",  " + (hand0)

    hand1 = ranks(player1)
    myHand = player1[0] + " " + player1[1] + " " + player1[2] + " " + player1[3] + " " + player1[4]
    print "%s\'s hand is:" % (players[1])
    print "       " + (myHand) + ",  " + (hand1)
    
    if len(player2) > 0:
        hand2 = ranks(player2)
        myHand = player2[0] + " " + player2[1] + " " + player2[2] + " " + player2[3] + " " + player2[4]
        print "%s\'s hand is:" % (players[2])
        print "       " + (myHand) + ",  " + (hand2)
        
    if len(player3) > 0:
        hand3 = ranks(player3)
        myHand = player3[0] + " " + player3[1] + " " + player3[2] + " " + player3[3] + " " + player3[4]
        print "%s\'s hand is:" % (players[3])
        print "       " + (myHand) + ",  " + (hand3)
        
    if len(player4) > 0:
        hand4 = ranks(player4)
        myHand = player4[0] + " " + player4[1] + " " + player4[2] + " " + player4[3] + " " + player4[4]
        print "%s\'s hand is:" % (players[4])
        print "       " + (myHand) + ",  " + (hand4)

##    playagain()
    pass

def start():
    print ""
    print ""
    print "Let's play a game of draw poker"
    print ""
    pick_players()
    game()


if __name__ == '__main__':
    start()
