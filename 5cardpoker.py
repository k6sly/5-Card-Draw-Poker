#!/usr/bin/env python2

#  First attempt at writing a 5 card draw poker game

import os
import random
import time
from poker_dict import *

#global variables
wcards = []
players = []
player0 = []
hand0 = []
player0_score = 0
player0_hands = 0
player1 = []
hand1 = []
player1_score = 0
player1_hands = 0
player2 = []
hand2 = []
player2_score = 0
player2_hands = 0
player3 = []
hand3 = []
player3_score = 0
player3_hands = 0
player4 = []
hand4 = []
player4_score = 0
player4_hands = 0


## These are set back to null just in case the player chooses to play again.  
def initialize():
    os.system('cls')
    print
    print
    print " Let's play a game of draw poker"
    print
    global wcards, player0, player1, player2, player3, player4, hand0, hand1, hand2, hand3, hand4
    del wcards[:]
    del player0[:]
    del player1[:]
    del player2[:]
    del player3[:]
    del player4[:]
    del hand0[:]
    del hand1[:]
    del hand2[:]
    del hand3[:]
    del hand4[:]

##    Here we ask for the player's name and how many opponents they want
def pick_players():
    global players
    if len(players) > 0:
        del players[:]
    player = raw_input(" What is your name? ")
    players.append(player)
    
    strPlayers = raw_input(" How many computer players (up to four)? ")
    if strPlayers in ('1','2','3','4'):
        numPlayers = int(strPlayers)
    else:
        print " %s is an invalid entry, please try again" % strPlayers
        start()
    print

##    Here we assign computer opponent names from the list called compNames imported from poker_dict.py
    for x in range(0,numPlayers):
        players.append(compNames[random.randint(0, len(compNames) - 1)])
        print " Computer player %s added" % players[x+1]
        print
        time.sleep(1)
		
    print " Shuffling..."
    time.sleep(3)
	

## The user is given the option to play again from the begining or using the same players
def playagain():
    print
    replay = raw_input("Do you want to play again Y/N? ")
    if replay in ("Y", "y", "YES", "Yes", "yes"):
        sameplayers = raw_input("Same Players Y/N? ")
        if sameplayers in ("Y", "y", "YES", "Yes", "yes"):
            initialize()
            return replay
        else:
            scores()
            print
            print " You are changing players, here are the scores for this session"
            print " Display of scores. We will continue in 10 seconds"
            time.sleep(10)
            start()
    else:
        pass
    

## This routine will change the face of the card to an integer or face value from an integer
## in the case of a flush we must provide a provision to retrun the same value, as we don't know
## what the final outcome will be in the printed value.
def ck_card(face, direction):
    if direction == 'decode':
        if face in ("A","K","Q","J"):
            x = facecard[face]
        else:
            x = int(face)
    else:
        if face in ("spades", "hearts", "diamonds", "clubs"):
            x = face         
        elif face > 10:
            x = cardface[face]           
        else:
            x = str(face)

    return x

## This routine is used to replace cards in the HUMAN player's hand. You can replace up to 5 cards  
def replace_cards(myHand):  
    global player0
    v = []
    x = 0
    a = 0
    t = 0
    print " You may replace up to 5 cards. Enter the number of the cards to replace one at a time "
    ## This range is needed in case the user picks the wrong card one or more times (x cannot be manipulated after the FOR
    ## therefore t is used to count the number of cards removed.)
    for x in range(0,12):
        if t == 0:
            a = '1st'
        elif t == 1:
            a = '2nd'
        elif t == 2:
            a = '3rd'
        elif t == 3:
            a = '4th'
        elif t == 4:
            a = '5th'
        replaceCard = raw_input(" %s card to replace ( press enter with no card when done ) " % a)
        if replaceCard == '':   ## This ends the selection of cards
            break
        if replaceCard in ('1','2','3','4','5') and replaceCard not in v:  ## Checks if the card is between 1-5 and if it has already been selected.
            v.append(replaceCard) ## adds the selected card to the "v" list
            t += 1 ## incremented to select the next card
        elif replaceCard in v:
            print " You already chose that card (" + player0[int(replaceCard)-1] + ")"
        else:    
            print " You entered an invalid card number"
            print " Please try again"

        if t == 5:
            break
                
    if len(v) > 0:
        for x in range(0,len(v)):
            b = int(v[x]) - 1  ## Will corespond with the selected card in the player0 list
            player0[b] = wcards.pop(random.randint(0, len(wcards) - 1))  ## Selects a new random card from wcards and assings it to the player0 list

## Used to break ties in winning hands by selecting cards to to compare in the calling routine.            
def win_tie(s, x):
    count = 0
    b = []
    while count < len(s):
        if s[count] == 0:
            a = hand0[x]
        if s[count] == 1:
            a = hand1[x]
        if s[count] == 2:
            a = hand2[x]
        if s[count] == 3:
            a = hand3[x]
        if s[count] == 4:
            a = hand4[x]
        b.append(a)
        count += 1
    return b

# This routine will return the outcome of a hand in an ordered list. [0] = the rank 1-10, [1] = highest card, pair, or suit, [2] = other pertaining information.
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
    outcome = []
    
    for x in hand:
        card = x
        if len(card) == 3:
            cardN = ck_card(card[0:2], 'decode')
            cardT = card[2]
        else:
            cardN = ck_card(card[0], 'decode')
            cardT = card[1]

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

## Five of the same suit is a flush
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
## Five cards in a row is a strait.
    for r in xrange(0, len(numPair)-1):
        if numPair[r+1] - numPair[r] != 1:
            strait = 0
        else:
            strait += 1
    
## Here we look for pairs, three of a kind and four of a kind (quads) and full houses
        likecards = numPair.count(numPair[r])
        if likecards == 4:
            pair1 = numPair[r]
            break
        if likecards == 3:
        if likecards == 2:
                pair2 = numPair[r]
            elif pair1 > 0:
            else:
                
        if numPair[4] - numPair[3] == 1:
        outcome.append(suit)
        outcome.append(9)
        outcome.append(suit)
        outcome.append(numPair[4])
        outcome.append(8)
        outcome.append(pair1)
        outcome.append(7)
        outcome.append(three)
            outcome.append(pair2)
        else:
            outcome.append(pair1)
        outcome.append(6)
        outcome.append(suit)
        outcome.append(numPair[4])
        outcome.append(5)
        outcome.append(numPair[4])
        outcome.append(4)
        outcome.append(three)
    elif pair1 != 0 and pair2 != 0 and pair1 != pair2:
        if pair1 > pair2:
            outcome.append(pair1)
            outcome.append(pair2)
        else:
            outcome.append(pair2)
            outcome.append(pair1)
        outcome.append(2)
        outcome.append(pair1)
        if numPair[4] == pair1:
            outcome.append(numPair[2])
        else:
            outcome.append(numPair[4])
        outcome.append(1)
        outcome.append(numPair[4])
        outcome.append(numPair[3])
        outcome.append(numPair[2])
        outcome.append(numPair[1])
        outcome.append(numPair[0])
    else:
        outcome = 'An Error has occurred'

    return outcome

def findExtra(hand):
    s = []
    s = hand
    rank = s[0]
    
    if rank == 1:
        p1 = ck_card(s[1], 'encode')
        p1 += ' High with '
        p1 += ck_card(s[2], 'encode')
        p1 += ', ' + ck_card(s[3], 'encode')
        p1 += ', ' + ck_card(s[4], 'encode')
        p1 += ', ' + ck_card(s[5], 'encode')
    elif rank == 2:
        if s[2] == 8 or s[2] == 14:
            p1 = ck_card(s[1], 'encode') + '\'s with an ' + ck_card(s[2], 'encode')
        else:
            p1 = ck_card(s[1], 'encode') + '\'s with a ' + ck_card(s[2], 'encode')
    elif rank == 3:
        p1 = ck_card(s[1], 'encode') + '\'s and ' + ck_card(s[2], 'encode') +  '\'s'
    elif  rank == 4:
        p1 = ck_card(s[1], 'encode') + '\'s '
    elif rank == 5:
        p1 = ' to the ' + ck_card(s[1], 'encode')
    elif rank == 6 or rank == 9:
        p1 ='in ' + s[1] +' to the ' + ck_card(s[2], 'encode')
    elif rank == 7:
        p1 = ck_card(s[1], 'encode') + ' Full of ' + ck_card(s[2], 'encode') + '\'s'
    elif rank == 8:
        p1 = ck_card(s[1], 'encode') +' \'s'
    elif rank == 10:
        p1 = ' in' + s[1]
    
    return p1
    
def game():
    global wcards, player0, player1, player2, player3, player4
    global hand0, hand1, hand2, hand3, hand4
    global player0_hands, player1_hands, player2_hands, player3_hands, player4_hands
    global player0_score, player1_score, player2_score, player3_score, player4_score
    os.system('cls')
    print " " + players[0] + "'s hand:"
    for x in range(0,5):
        player0.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        time.sleep(0.5)
        player1.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        if n > 2:
            player2.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        if n > 3:
            player3.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        if n > 4:
            player4.append(wcards.pop(random.randint(0, len(wcards) - 1)))

    myHand = player0[0] + " " + player0[1] + " " + player0[2] + " " + player0[3] + " " + player0[4]
    if replace in ("Y", "y", "YES", "Yes", "yes"):
        replace_cards(myHand)
        myHand = player0[0] + " " + player0[1] + " " + player0[2] + " " + player0[3] + " " + player0[4]
        os.system('cls')
        print " " + players[0] + "'s hand:"
        for x in range(0,5):
            time.sleep(0.5)
    elif replace in ("N", "n", "NO", "No", "no"):
        pass
        print " Your answer was not appropriate. You answered " + replace + ". Moving on!"
        print
            
    print " %s\'s hand is:" % (players[0])
    
    player1_hands += 1
    myHand = player1[0] + " " + player1[1] + " " + player1[2] + " " + player1[3] + " " + player1[4]
    print " %s\'s hand is:" % (players[1])
        
    if n > 2:
        player2_hands += 1
        myHand = player2[0] + " " + player2[1] + " " + player2[2] + " " + player2[3] + " " + player2[4]
        print " %s\'s hand is:" % (players[2])
    
    if n > 3:
        player3_hands += 1
        myHand = player3[0] + " " + player3[1] + " " + player3[2] + " " + player3[3] + " " + player3[4]
        print " %s\'s hand is:" % (players[3])
    
    if n > 4:
        player4_hands += 1
        myHand = player4[0] + " " + player4[1] + " " + player4[2] + " " + player4[3] + " " + player4[4]
        print " %s\'s hand is:" % (players[4])

    if n == 5:
    elif n == 4:
        playerRanks = [hand0[0], hand1[0], hand2[0], hand3[0]]
    elif n == 3:
        playerRanks = [hand0[0], hand1[0], hand2[0]]
    elif n == 2:
        playerRanks = [hand0[0], hand1[0]]
        
    if count > 1:
        s = []
            if playerRanks[w] == tempRanks:
                s.append(w)
            if 0 in s:
                player0_score += 1
            if 1 in s:
                player1_score += 1
            if 2 in s:
                player2_score += 1
            if 3 in s:
                player3_score += 1
            if 3 in s:
                player4_score += 1
            count = t.count(max(t))
            if count > 1:
                u = t
                l = len(u)
                for x in range(0, l):
                    if u[x] == max(u):
            
        x = 0
        l = len(t)
        z = []
            if top < t[x+1]:
                top = t[x+1]
    else:
    
    if y == 0:
        player0_score += 1
    elif y == 1:
        z = hand1
        player1_score += 1
    elif y == 2:
        z = hand2
        player2_score += 1
    elif y == 3:
        z = hand3
        player3_score += 1
    elif y == 4:
        z = hand4
        player4_score += 1
        
    print
    print winner
    return playagain()
    pass


def start():
    initialize()
    pick_players()
        pass
    scores()

def scores():
    global players, player0_score, player1_score, player2_score, player3_score, player4_score
    global player0_hands, player1_hands, player2_hands, player3_hands, player4_hands
    os.system('cls')
    print
    print " Thank you for playng 5 card draw poker"
    print
    print " HIGH SCORES"
    print "    Human: " + players[0].ljust(10) + " Hands: " + str(player0_hands) + " Score " + str(player0_score)
    print " Computer: "+ players[1].ljust(10) + " Hands: " + str(player1_hands) + " Score " + str(player1_score)
    count = len(players)
    if count > 2:
        print " Computer: "+ players[2].ljust(10) + " Hands: " + str(player2_hands) + " Score " + str(player2_score)
    if count > 3:
        print " Computer: "+ players[3].ljust(10) + " Hands: " + str(player3_hands) + " Score " + str(player3_score)
    if count > 4:
        print " Computer: "+ players[4].ljust(10) + " Hands: " + str(player4_hands) + " Score " + str(player4_score)
	

if __name__ == '__main__':
    start()
