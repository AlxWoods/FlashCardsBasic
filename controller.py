import csv
import pandas as pd
import random
import numpy as np

class Cards():
    def __init__(self,filename,card_list=[],card_deck=[],card_side = True,current_card = 0,weighted_list=[]):
        self.filename = filename
        self.card_list = card_list
        self.card_deck = card_deck
        self.card_side = card_side          #displays current side
        self.current_card = current_card    
        self.weighted_list = weighted_list  #frequency of each card randomly chosen
        self.study_deck_size = 5            #number of cards in the set
        self.numb_of_decks=0                #total number of sets
        self.current = 0                    #current set

    def nest_list(self,list1,rows,columns):
        result=[]
        start = 0
        end = columns
        for i in range(rows):
            result.append(list1[start:end])
            start +=columns
            end += columns
        return result

    def make_deck(self):
        with open(self.filename,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            full_card_deck = []
            for line in csv_reader:
                full_card_deck.append(line)
                #self.card_list.append(line)
            random.shuffle(full_card_deck)
            self.numb_of_decks = self.determine_size(len(full_card_deck))
            self.card_deck = self.nest_list(full_card_deck,self.numb_of_decks,self.study_deck_size)
            self.set_card_list()
            return 
        
    def determine_size(self,val):
        while val % self.study_deck_size != 0:
            val += 1
        return int(val / self.study_deck_size)

    def set_card_list(self):
        self.card_list = self.card_deck[self.current]
        for x in self.card_list:
            if x == '':
                self.card_list.remove('')
        self.make_card_weight()
        print(self.card_list)
        return

    def next_c(self):
        if self.current + 1 < self.numb_of_decks:
            self.current += 1
        self.set_card_list()
        return

    def prev_c(self):
        if self.current > 0:
            self.current -= 1
        self.set_card_list()

    def get_card_text(self,x):
        display_card = []

        if self.card_side == True:
            display_card.append(self.card_list[x][0])
            display_card.append(self.card_list[x][2])

        elif self.card_side == False:
            display_card.append(self.card_list[x][1])
            display_card.append(self.card_list[x][3])

        return display_card
    
    def flip_card(self):
        if self.card_side == True:
            self.card_side = False
        elif self.card_side == False:
            self.card_side = True

    def make_card_weight(self):
        #create and populate a list
        ran_list = [[0 for i in range(2)] for j in range(len(self.card_list))]
        for i in range(0,len(ran_list)):
            ran_list[i][0] = i

        #Creates weights for each value
        for i in range(0,len(ran_list)):
            ran_list[i][1] = int((0.1 * (i * i) + 3))
        self.weighted_list = ran_list
        return 

    def get_random_card(self):
        curr = self.current_card
        ind,weight=zip(*self.weighted_list)
        print(weight)
        x = random.choices(ind, weights=weight, k=1)
        while True:
            if self.current_card != x[0]:
                break
            x = random.choices(ind, weights=weight, k=1)

        self.current_card = x[0]


    def next_card(self):
        self.get_random_card()
        return
    
    def raise_card(self, raise_c):
        end_list = len(self.card_list) - 1

        if self.current_card < end_list and raise_c == True:
            temp = self.card_list[self.current_card]
            x = self.current_card + 1
            self.card_list[self.current_card] = self.card_list[x]
            self.card_list[x] = temp
        
        elif self.current_card > 0 and raise_c == False:
            temp = self.card_list[self.current_card]
            x = self.current_card - 1
            self.card_list[self.current_card] = self.card_list[x]
            self.card_list[x] = temp

        for x in self.card_list:
            print(x)
        print(self.current_card)
        print(self.weighted_list[self.current_card])
        return