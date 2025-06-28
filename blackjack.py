
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
while 1 == 1:
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
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU LOST')
            playermoney = playermoney / 2
            print('you have $', playermoney, '\n\n\n\n\n')
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
        elif cardsbot >= 22:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU WON')
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n')
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
        if cardsplayer == 21:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU WON')
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
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
        elif cardsplayer >= 22:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU LOST')
            playermoney = playermoney / 2
            print('you have $', playermoney, '\n\n\n\n\n')
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
    elif ch == '2':
        print(cardsbot, ' - dealer', cardsplayer, ' - yours')
        if cardsplayer >= cardsbot:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)            
            input('you won')
            playermoney = playermoney * 2
            print('you have $', playermoney, '\n\n\n\n\n')
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
        else:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('you lost')
            playermoney = playermoney / 2
            print('you have $', playermoney, '\n\n\n\n\n')
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
    elif ch == 'cheat.enable("console_override")':
        print('\n\n\n\n\n\n             you enabled cheats, you cheater... :( \n\n\n\n\n\n')
        for cheatx in range(99):
            playermoney = playermoney * cheatx * cheatx + cheatx
            print(' little cheater got $', playermoney, ' now', end = '')
        ch == ''
    elif ch == '0':
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
    elif ch == 'chnum':
        playermoney = input("set money:")
        playermoney = int(playermoney)
        print(playermoney)

    else:
        print('try again please\n\n\n')
