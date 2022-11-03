from ast import And
import csv
from fileinput import filename
from pickle import TRUE
import pandas as pd
import random

class Cards():
    def __init__(self,filename,card_list=[],card_side = True,current_card = 0,weighted_list=[]):
        self.filename = filename
        self.card_list = card_list          
        self.card_side = card_side          #boolean for whether or not the care is facing upward
        self.current_card = current_card  
        self.weighted_list = weighted_list  

    def make_card_list(self):
        with open(self.filename,'r') as csv_file:
            csv_reader  = csv.reader(csv_file)
            
            next(csv_reader)
            self.card_list = []

            for line in csv_reader:
                self.card_list.append(line)
            return 

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


#c = Cards('data/words.csv')
#c.make_card_list()
#print(c.get_card_text(0))
#print(c.get_card_text(0))
