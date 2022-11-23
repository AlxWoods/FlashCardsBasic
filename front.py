from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
import controller


c = controller.Cards('data/words.csv')
c.make_deck(True)
c.make_card_weight()


window = Tk()
window.title("Flash Cards")
window.geometry("400x200")
window.minsize(400, 130)
window.maxsize(400, 130)

card_text = "Click Here\nto Start"

def card_button_click():
    after_start()
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
    print(card_text)

def raise_card():
    c.raise_card(True)
    next_card()

def lower_card():
    c.raise_card(False)
    next_card()

def after_start():
    next_button['state'] = NORMAL
    raise_button['state'] = NORMAL
    lower_button['state'] = NORMAL
    #btn1['state'] = DISABLED

card_button = Button(window, text = card_text, 
                        command = card_button_click) #,padx = 100,pady = 50
next_button = Button(window, text = "Next Card",state = DISABLED,
                        command = next_card)
raise_button = Button(window, text = "Difficult",state = DISABLED,
                        command = raise_card)
lower_button = Button(window, text = "Easy",state = DISABLED,
                        command = lower_card)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)


card_button.grid(row = 0,column = 0,columnspan = 3)
raise_button.grid(row = 1,column = 2)
next_button.grid(row = 1,column = 1,padx=5, pady=5)
lower_button.grid(row = 1,column = 0)

my_menu = Menu(window)
window.config(menu=my_menu)

#menu methods
def get_file(): 
    window.filename = filedialog.askopenfilename(initialdir='data/', title='Select a File')
    c.filename = window.filename
    c.make_deck(False)
    return


def save_file():
    f = filedialog.asksaveasfile(initialdir='data/',initialfile = 'Untitled.csv',defaultextension=".csv",filetypes=[("csv","*.csv")])
    if f != None:
        file_name = ''
        for f_char in reversed(f.name):
            if f_char == '/':
                break
            file_name = file_name + f_char
        c.save_deck(file_name[::-1])

def prev_cards():
    card_change = c.current
    c.prev_c()
    if card_change == c.current:
        showinfo("Card Set Error", "Couldn't Go to Previous Set")

def next_cards():
    card_change = c.current
    c.next_c()
    if card_change == c.current:
        showinfo("Card Set Error", "Couldn't Go to Next Set")

def display_current_cards():
    pass

#create menu
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open File", command=get_file)
file_menu.add_command(label="Exit", command=window.quit)

cards_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Cards", menu=cards_menu)
cards_menu.add_command(label="Previous Card Set", command=prev_cards)
cards_menu.add_command(label="Next Card Set", command=next_cards)
cards_menu.add_command(label="Display Current Cards", command=display_current_cards)

window.mainloop()