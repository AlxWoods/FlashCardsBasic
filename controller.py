import csv
from fileinput import filename
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
        ind,weight=zip(*self.weighted_list)
        
        r = random.randint(1, max(weight))
        for char, we  in self.weighted_list:
            temp = r - we 
            if temp <= 0:
                card_number = char
                break
        return card_number

    def next_card(self):
        self.make_card_weight()
        self.current_card = self.get_random_card()
        return
    


#c = Cards('data/words.csv')
#c.make_card_list()
#print(c.get_card_text(0))
#print(c.get_card_text(0))
