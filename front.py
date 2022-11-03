from tkinter import *
import controller


c = controller.Cards('data/words.csv')
c.make_card_list()
c.make_card_weight()


window = Tk()
window.title("Flash Cards")
window.geometry("400x200")

card_text = "Click Here\nto Start"

def card_button_click():
    c.flip_card()
    get_text()
    
    
def next_card():
    #c.make_card_weight()
    #c.raise_card(True)
    c.next_card()
    get_text()

def get_text():
    card_text = c.get_card_text(c.current_card)
    t = '{}\n\n{}'.format(card_text[0],card_text[1])
    card_button.config(text = t)

def raise_card():
    c.raise_card(True)
    next_card()

def lower_card():
    c.raise_card(False)
    next_card()



card_button = Button(window, text = card_text, command = card_button_click) #,padx = 100,pady = 50
next_button = Button(window, text = "Next Card",command = next_card)

raise_button = Button(window, text = "Difficult",command = raise_card)
lower_button = Button(window, text = "Easy",command = lower_card)


card_button.pack()
next_button.pack()

raise_button.pack()
lower_button.pack()


window.mainloop()