


def blackjack_new():
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
    def init_round():
        global cardsplayer, cardsbot, firstcard, secondcard, dealersfirstcard
        cardsplayer = random.randint(5,10)
        firstcard = cardsplayer
        secondcard = random.randint(5,10)
        cardsplayer = firstcard + secondcard
        cardsbot = random.randint(5,10)
        dealersfirstcard = cardsbot
        cardsbot += random.randint(5,10)

    init_round()

    # Entry widget for user input
    entry = tk.Entry(root)
    entry.pack()

    def clear_screen():
        for widget in root.winfo_children():
            widget.destroy()
        
        global entry
        entry = tk.Entry(root)
        entry.pack()
        tk.Button(root, text="Submit", command=process_input).pack()

    def aftergame():
        global record, mostplayermoney, playermoney
        if mostplayermoney > playermoney:
            record = mostplayermoney
        elif mostplayermoney <= playermoney:
            record = playermoney
            mostplayermoney = playermoney
        
        init_round()  # This will reset all card values including dealersfirstcard
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
        global cardsplayer, cardsbot
        
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

            process_input()
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


def old_blackjack():
    print('get as close as possible to 21 without going over it \n you dont know the dealers number of total cards \n you can stop if you think you are closer to 21 than the dealer \n')
    import random
    cardsplayer = 0
    cardsbot = 0
    randomvalue = 0
    cardsplayer = cardsplayer + random.randint(5,10)
    firstcard = cardsplayer
    secondcard = random.randint(5,10)
    cardsplayer = firstcard + secondcard
    cardsbot = cardsbot + random.randint(5,10)
    dealersfirstcard = cardsbot
    cardsbot = cardsbot + random.randint(5,10)
    playermoney = 500
    mostplayermoney = playermoney
    record = playermoney
    def aftergame():
        global record
        global randomvalue
        global dealersfirstcard
        global cardsplayer
        global cardsbot
        global randomvalue
        global firstcard
        global secondcard
        global mostplayermoney
        
        if mostplayermoney > playermoney:
            record = mostplayermoney
        elif mostplayermoney <= playermoney:
            record = playermoney
            mostplayermoney = playermoney
        cardsplayer = 0
        cardsbot = 0
        randomvalue = 0
        cardsplayer = cardsplayer + random.randint(5,10)
        firstcard = cardsplayer
        secondcard = random.randint(5,10)
        cardsplayer = firstcard + secondcard
        cardsbot = cardsbot + random.randint(5,10)
        dealersfirstcard = cardsbot
        cardsbot = cardsbot + random.randint(5,10)
    while 1 == 1:
        print("your record is: ", record)
        print('your current money: ', playermoney)
        print('dealers first card - ', dealersfirstcard)
        print('your first card - ', firstcard, ' and your second card - ', secondcard) 
        print('your total cards - ', cardsplayer)
        ch = input(' [1] - to get a card (1 to 10) \n [2] - to bust the cards \n [0] - to reset the match \n $>  ')
        if ch == '1':
            thirdcard = random.randint(1,9)
            cardsplayer = cardsplayer + thirdcard
            print('\n           the third card you got is.... - ', thirdcard, '   \n')
            cardsbot = cardsbot + random.randint(1,9)
            if cardsbot == 21:
                playermoney = playermoney / 2
                print('you have $', playermoney)
                print('you got', cardsplayer)
                print('and dealer got', cardsbot)
                input('YOU LOST\n\n\n')

                aftergame()
                
            elif cardsbot >= 22:
                playermoney = playermoney * 2
                print('you have $', playermoney)
                print('you got', cardsplayer)
                print('and dealer got', cardsbot)
                input('YOU WON\n\n\n')
                beforeplayermoney = playermoney

                aftergame()
            if cardsplayer == 21:
                playermoney = playermoney * 2
                print('you have $', playermoney)
                print('you got', cardsplayer)
                print('and dealer got', cardsbot)
                input('YOU WON\n\n\n')
                beforeplayermoney = playermoney
                aftergame()
            elif cardsplayer >= 22:
                playermoney = playermoney / 2
                print('you have $', playermoney)
                print('you got', cardsplayer)
                print('and dealer got', cardsbot)
                input('YOU LOST\n\n\n')
                beforeplayermoney = playermoney

                aftergame()
        elif ch == '2':
            print(cardsbot, ' - dealer', cardsplayer, ' - yours')
            if cardsplayer >= cardsbot:
                playermoney = playermoney * 2
                print('you have $', playermoney)
                print('you got', cardsplayer)
                print('and dealer got', cardsbot)            
                input('YOU WON\n\n\n')
                beforeplayermoney = playermoney

                aftergame()
            else:
                playermoney = playermoney / 2
                print('you have $', playermoney)
                print('you got', cardsplayer)
                print('and dealer got', cardsbot)
                input('YOU LOST\n\n\n')

                aftergame()
        elif ch == 'cheat.getmoney':
            print('\n\n\n\n\n\n             you enabled cheats, you cheater... :( \n\n\n\n\n\n')
            for cheatx in range(99):
                playermoney = playermoney * cheatx * cheatx + cheatx
                print(' little cheater got $', playermoney, ' now', end = '')
            ch == ''
        elif ch == '0':
            aftergame()
        elif ch == 'cheat.chnum':
            playermoney = input("set money:")
            playermoney = int(playermoney)
            print(playermoney)
        elif ch == "cheat.win":
            cardsplayer = 21
        elif ch == 'cheat.loose':
            cardsplayer = 1
        elif ch == 'cheat.setcards':
            cardsplayer = input('how many cards')
        elif ch == 'cheat.clear':
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        else:
            print('try again please\n\n\n')



blackjack_new()
