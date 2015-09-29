#!/usr/bin/env python2

#  First attempt at writing a 5 card draw poker game

import random
import os
import time
from poker_dict import *

wcards = []
players = []
player0 = []
player1 = []
player2 = []
player3 = []
player4 = []
hand0 = []
hand1 = []
hand2 = []
hand3 = []
hand4 = []

def initialize():
    os.system('cls')
    print ""
    print ""
    print "Let's play a game of draw poker"
    print ""
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

def pick_players():
##    Here we ask for the player's name and how many opponents they want
    global players
    player = raw_input("What is your name? ")
    players.append(player)
    
    strPlayers = raw_input("How many computer players (up to four)? ")
    if strPlayers in ('1','2','3','4'):
        numPlayers = int(strPlayers)
    else:
        print "%s is an invalid entry, please try again" % strPlayers
        start()
    print
##    Here we assign computer opponent names from the list called compNames
    for x in range(0,numPlayers):
        players.append(compNames[random.randint(0, len(compNames) - 1)])
        print "Computer player %s added" % players[x+1]
        print

def playagain():
    print
    replay = raw_input("Do you want to play again Y/N? ")
    if replay in ("Y", "y", "YES", "Yes"):
        sameplayers = raw_input("Same Players Y/N? ")
        if sameplayers in ("Y", "y", "YES", "Yes"):
            initialize()
            game()
        else:
            start()
    else:
        quit()

def replace_cards(myHand):
    global player0
    v = []
    x = 0
    print "You may replace up to 5 cards. Enter cards to replace one at a time ( example Kd ) "
    for x in range(0,5):
        if x == 0:
            a = '1st'
        elif x == 1:
            a = '2nd'
        elif x == 2:
            a = '3rd'
        elif x == 3:
            a = '4th'
        elif x == 4:
            a = '5th'
        replaceCard = raw_input("%s card to replace ( press enter with no card when done ) " % a)
        if replaceCard == '':
            break
        cardN = replaceCard[0]
        cardT = replaceCard[1]
        replaceCard = cardN.upper() + cardT.lower()
        if replaceCard in player0:
            v.append(replaceCard)
        else:
            print "You entered an invalid card " + replaceCard + " is not in your hand (" + myHand + ")"
            print "Please try again"
            replace_cards(myHand)
                
    if len(v) > 0:
        for x in range(0,len(v)):
            b = player0.index(v[x])
            player0[b] = wcards.pop(random.randint(0, len(wcards) - 1))
            
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

        likecards = numPair.count(numPair[r])
        if likecards == 4:
            pair1 = numPair[r]
            break
        if likecards == 3:
            three = numPair[r]
        if likecards == 2:
            if three > 0:
                pair2 = numPair[r]
            elif pair1 > 0:
                pair2 = numPair[r]
            else:
                pair1 = numPair[r]
                
    if strait == 4:
        if numPair[4] - numPair[3] == 1:
            strait += 1
        
    if flush == 1 and strait == 5 and count == 60:
        outcome.append(10)
        outcome.append(suit)
    elif flush == 1 and strait == 5:
        outcome.append(9)
        outcome.append(suit)
        outcome.append(numPair[4])
    elif likecards == 4:
        outcome.append(8)
        outcome.append(pair1)
    elif three != 0 and (pair1 != 0 or pair2 != 0):
        outcome.append(7)
        outcome.append(three)
        if three == pair1:
            outcome.append(pair2)
        else:
            outcome.append(pair1)
    elif flush == 1:
        outcome.append(6)
        outcome.append(suit)
        outcome.append(numPair[4])
    elif strait == 5:
        outcome.append(5)
        outcome.append(numPair[4])
    elif three != 0:
        outcome.append(4)
        outcome.append(three)
    elif pair1 != 0 and pair2 != 0 and pair1 != pair2:
        outcome.append(3)
        if pair1 > pair2:
            outcome.append(pair1)
            outcome.append(pair2)
        else:
            outcome.append(pair2)
            outcome.append(pair1)
    elif pair1 != 0:
        outcome.append(2)
        outcome.append(pair1)
        if numPair[4] == pair1:
            outcome.append(numPair[2])
        else:
            outcome.append(numPair[4])
    elif pair1 == 0:
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
    global wcards, player0, player1, player2, player3, player4, hand0, hand1, hand2, hand3, hand4
    n = len(players)
    wcards = cards[:]
    os.system('cls')
    for x in range(0,5):
        player0.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        print cardsGraph[player0[x]]
        time.sleep(0.5)
        player1.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        if n > 2:
            player2.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        if n > 3:
            player3.append(wcards.pop(random.randint(0, len(wcards) - 1)))
        if n > 4:
            player4.append(wcards.pop(random.randint(0, len(wcards) - 1)))
##    player0 = ["4d", "Qc", "Ac", "9d", "Jh"]
##    player1 = ["2c", "Js", "3s", "6d", "Qs"]
##    player2 = ["As", "8s", "5h", "4c", "Kc"]
##    player4 = ["7d", "9s", "4s", "10s", "3c"]
##    player3 = ["10d", "Qd", "2h", "7c", "5c"]

    myHand = player0[0] + " " + player0[1] + " " + player0[2] + " " + player0[3] + " " + player0[4]
    replace = raw_input("Would you like to draw/replace any cards %s Y/N? " % myHand)
    if replace in ("Y", "y", "YES", "Yes"):
        replace_cards(myHand)
        myHand = player0[0] + " " + player0[1] + " " + player0[2] + " " + player0[3] + " " + player0[4]
        os.system('cls')
        for x in range(0,5):
            print cardsGraph[player0[x]]
            time.sleep(0.5)
    elif replace in ("N", "n", "NO", "No"):
        pass
    else:
        print "Your answer was not appropriate. You answered " + replace + ". Moving on!"
        print
            
    hand0 = ranks(player0)
    print "%s\'s hand is:" % (players[0])
    print "       " + (myHand) + ",  " + hands[hand0[0]] + '( ' + ck_card(hand0[1],'encode') + ' )'
    
    hand1 = ranks(player1)
    myHand = player1[0] + " " + player1[1] + " " + player1[2] + " " + player1[3] + " " + player1[4]
    print "%s\'s hand is:" % (players[1])
    print "       " + (myHand) + ",  " + hands[hand1[0]] + '( ' + ck_card(hand1[1],'encode') + ' )'
        
    if n > 2:
        hand2 = ranks(player2)
        myHand = player2[0] + " " + player2[1] + " " + player2[2] + " " + player2[3] + " " + player2[4]
        print "%s\'s hand is:" % (players[2])
        print "       " + (myHand) + ",  " + hands[hand2[0]] + '( ' + ck_card(hand2[1],'encode') + ' )'
    
    if n > 3:
        hand3 = ranks(player3)
        myHand = player3[0] + " " + player3[1] + " " + player3[2] + " " + player3[3] + " " + player3[4]
        print "%s\'s hand is:" % (players[3])
        print "       " + (myHand) + ",  " + hands[hand3[0]] + '( ' + ck_card(hand3[1],'encode') + ' )'
    
    if n > 4:
        hand4 = ranks(player4)
        myHand = player4[0] + " " + player4[1] + " " + player4[2] + " " + player4[3] + " " + player4[4]
        print "%s\'s hand is:" % (players[4])
        print "       " + (myHand) + ",  " + hands[hand4[0]] + '( ' + ck_card(hand4[1],'encode') + ' )'

    if n == 5:
        playerRanks = [hand0[0], hand1[0], hand2[0], hand3[0], hand4[0]]
    elif n == 4:
        playerRanks = [hand0[0], hand1[0], hand2[0], hand3[0]]
    elif n == 3:
        playerRanks = [hand0[0], hand1[0], hand2[0]]
    elif n == 2:
        playerRanks = [hand0[0], hand1[0]]
        
    tempRanks = max(playerRanks)
    count = playerRanks.count(tempRanks)
    if count > 1:
        s = []
        for w in range(0, len(playerRanks)):
            if playerRanks[w] == tempRanks:
                s.append(w)
        if tempRanks == 10:
            winner = 'we have a tie! ' + count + ' players have a Royal Flush. There must be some cheating going on here!'
        if tempRanks in (6,7,9):
            t = win_tie(s, 2)
        if tempRanks in (3,4,5,8):
            t = win_tie(s, 1)
        if tempRanks in (1,2):
            t = win_tie(s,1)
            count = t.count(max(t))
            if count > 1:
                u = t
                t = win_tie(s,2)
                l = len(u)
                for x in range(0, l):
                    if u[x] == max(u):
                        t[x] = max(u)+t[x]+100
            
        x = 0
        l = len(t)
        top = t[0]
        z = []
        for x in range(0,l-1):
            if top < t[x+1]:
                top = t[x+1]
        y = t.index(top)
        y = s[y]
    else:
        y = playerRanks.index(tempRanks)
    
    if y == 0:
        z = hand0
    elif y == 1:
        z = hand1
    elif y == 2:
        z = hand2
    elif y == 3:
        z = hand3
    elif y == 4:
        z = hand4
        
    winner = 'winner is ' + players[y] + ' with ' + hands[tempRanks] + ' ( ' + findExtra(z) + ' )'
    print
    print winner
    playagain()
    pass


def start():
    initialize()
    pick_players()
##    players.append('Scott')
##    players.append('Steve')
##    players.append('Looser')
##    numPlayers = 3
    game()

def quit():
    pass

if __name__ == '__main__':
    start()
