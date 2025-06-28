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
    
    if beforeplayermoney > playermoney:
        record = mostplayermoney
    elif beforeplayermoney < playermoney:
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
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU LOST')

            aftergame()
            
        elif cardsbot >= 22:
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU WON')
            beforeplayermoney = playermoney

            aftergame()
        if cardsplayer == 21:
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU WON')
            beforeplayermoney = playermoney
            aftergame()
        elif cardsplayer >= 22:
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU LOST')
            beforeplayermoney = playermoney

            aftergame()
    elif ch == '2':
        print(cardsbot, ' - dealer', cardsplayer, ' - yours')
        if cardsplayer >= cardsbot:
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)            
            input('YOU WON')
            beforeplayermoney = playermoney

            aftergame()
        else:
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU LOST')

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
    elif ch == 'cheat.clear':
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        print('try again please\n\n\n')
