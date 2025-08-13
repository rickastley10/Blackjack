import tkinter as tk
import random

root = tk.Tk()

# Override print to use Label
print = tk.Label

# Game instructions
print(root, text='get as close as possible to 21 without going over it \n you dont know the dealers number of total cards \n you can stop if you think you are closer to 21 than the dealer \n').pack()

# Game variables
cardsplayer = 0
cardsbot = 0
randomvalue = 0
playermoney = 500
mostplayermoney = playermoney
record = playermoney

# Initialize first round
cardsplayer = random.randint(5,10)
firstcard = cardsplayer
secondcard = random.randint(5,10)
cardsplayer = firstcard + secondcard
cardsbot = random.randint(5,10)
dealersfirstcard = cardsbot
cardsbot += random.randint(5,10)

# Entry widget for user input
entry = tk.Entry(root)
entry.pack()

def clear_screen():
    for widget in root.winfo_children():  # Get all widgets in the window
        widget.destroy()  # Destroy each widget
    
    # Recreate essential widgets (entry, etc.)
    global entry
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root, text="Submit", command=process_input).pack()

def aftergame():
    global record, cardsplayer, cardsbot, randomvalue, firstcard, secondcard, mostplayermoney, playermoney
    
    if mostplayermoney > playermoney:
        record = mostplayermoney
    elif mostplayermoney <= playermoney:
        record = playermoney
        mostplayermoney = playermoney
    
    # Reset game state
    cardsplayer = random.randint(5,10)
    firstcard = cardsplayer
    secondcard = random.randint(5,10)
    cardsplayer = firstcard + secondcard
    cardsbot = random.randint(5,10)
    dealersfirstcard = cardsbot
    cardsbot += random.randint(5,10)
    
    update_display()

def lost():
    global playermoney
    playermoney = playermoney // 2
    print(root, text=f'you have ${playermoney}').pack()
    print(root, text=f'you got {cardsplayer}').pack()
    print(root, text=f'and dealer got {cardsbot}').pack()
    print(root, text='YOU LOST\n\n\n').pack()
    aftergame()

def won():
    global playermoney
    playermoney = playermoney * 2
    print(root, text=f'you have ${playermoney}').pack()
    print(root, text=f'you got {cardsplayer}').pack()
    print(root, text=f'and dealer got {cardsbot}').pack()
    print(root, text='YOU WON\n\n\n').pack()
    aftergame()

def process_input():
    global cardsplayer, cardsbot, playermoney
    
    ch = entry.get()
    entry.delete(0, tk.END)
    
    if ch == '1':
        thirdcard = random.randint(1,9)
        cardsplayer += thirdcard
        print(root, text=f'\n the third card you got is.... - {thirdcard} \n').pack()
        cardsbot += random.randint(1,9)
        
        if cardsbot == 21:
            lost()
        elif cardsbot >= 22:
            won()
        elif cardsplayer == 21:
            won()
        elif cardsplayer >= 22:
            lost()
        else:
            update_display()
    
    elif ch == '2':
        print(root, text=f'{cardsbot} - dealer, {cardsplayer} - yours').pack()
        if cardsplayer >= cardsbot:
            won()
        else:
            lost()
    
    elif ch == 'cheat.getmoney':
        print(root, text='\n\n\n\n\n\n you enabled cheats, you cheater... :( \n\n\n\n\n\n').pack()
        for cheatx in range(1, 100):
            playermoney = playermoney * cheatx * cheatx + cheatx
            print(root, text=f' little cheater got ${playermoney} now').pack()
    
    elif ch == '0':
        aftergame()
    
    elif ch == 'cheat.chnum':
        playermoney = int(input("set money:"))
        print(root, text=str(playermoney)).pack()
    
    elif ch == "cheat.win":
        cardsplayer = 21
        update_display()
    
    elif ch == 'cheat.loose':
        cardsplayer = 1
        update_display()
    
    elif ch == 'cheat.setcards':
        cardsplayer = int(input('how many cards'))
        update_display()
    
    elif ch == 'cheat.clear':
        clear_screen()
    
    else:
        print(root, text='try again please\n\n\n').pack()

def update_display():
    clear_screen()
    print(root, text=f"your record is: {record}").pack()
    print(root, text=f'your current money: {playermoney}').pack()
    print(root, text=f'dealers first card - {dealersfirstcard}').pack()
    print(root, text=f'your first card - {firstcard} and your second card - {secondcard}').pack()
    print(root, text=f'your total cards - {cardsplayer}').pack()
    print(root, text=' [1] - to get a card (1 to 10) \n [2] - to bust the cards \n [0] - to reset the match \n $>  ').pack()

# Submit button
tk.Button(root, text="Submit", command=process_input).pack()

# Initial display
update_display()

tk.mainloop()
