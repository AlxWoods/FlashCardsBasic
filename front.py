from tkinter import *
import controller


c = controller.Cards('data/words.csv')
c.make_card_list()


window = Tk()
window.title("Flash Cards")
window.geometry("400x200")

card_text = "Click Here\nto Start"

def card_button_click():
    c.flip_card()
    get_text()
    
    
def next_card():
    c.next_card()
    get_text()

def get_text():
    card_text = c.get_card_text(c.current_card)
    t = '{}\n\n{}'.format(card_text[0],card_text[1])
    card_button.config(text = t)


card_button = Button(window, text = card_text, command = card_button_click) #,padx = 100,pady = 50
next_button = Button(window, text = "Next Card",command = next_card)

card_button.pack()
next_button.pack()


window.mainloop()