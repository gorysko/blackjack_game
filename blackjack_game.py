import random
#import itertools
#import sys
#from inspect import getmembers
#from pprint import pprint

class Deck:
    
    def __init__(self):
                
        suits = ['s','c','d','h']
        faces = ['6','7','8','9','T','J','Q','K','A']
        self.deck=[]
        for i in suits:
            for j in faces:
                self.deck.append(i+j)

    def toss(self):
        random.shuffle(self.deck)

    def pop(self):
        return  self.deck.pop()

    def cardName(self,card):
        suits = {'s':'Spades','c':'Clubs','d':'Diamonds','h':'Hearts'}
        faces = {'6':'6','7':'7','8':'8','9':'9','T':'10','J':'Jack','Q':'Queen','K':'King','A':'Ace'}
        return faces[card[1]]+' of ' + suits[card[0]]

    def cardValue(self,card):
        faces = {'6':6,'7':7,'8':8,'9':9,'T':10,'J':2,'Q':3,'K':4,'A':11}
        return faces[card[1]]


class Table():

    def __init__(self,deck):
        self.deck = deck
        self.total = 0

    def run(self,name):

        while True:
            card = self.deck.pop()
            print(name+' have got %s' % self.deck.cardName(card))
            self.total += self.deck.cardValue(card)
            if self.total > 21:
                print(name+' have overloaded')
                return False
            else:
                answer = input('Do you want additional card? Y/N')
                if answer == 'N' or answer == 'n':
                    return self.total
            
                
#pprint(getmembers(myDeck))

#f = myDeck.pop()
#print(myDeck.cardName(f))
#print(myDeck.cardValue(f))
ready = True
bill = 0
billdealer = 0

while ready:
    myDeck = Deck()
    myDeck.toss()
    print('You are player')
    myTable = Table(myDeck)
    bill = myTable.run('You')
    if bill:
        print("You are dealer")
        dealerTable = Table(myDeck)
        billdealer = dealerTable.run('DealerMan')

        if billdealer:
            if billdealer > bill:
                print ('You are looser {bill} < {deal}'.format(bill=bill, deal=billdealer ))
            else:
                print ('You are winner {bill} > {deal}'.format(bill=bill, deal=billdealer))
        else:
             print ('You are winner because dealer is greed')
    else:
        print ('You are looser because OVERLOADED')

    answer = input('Do you want additional Game? Y/N')
    if answer == 'N' or answer == 'n':
        break