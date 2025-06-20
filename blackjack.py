print('get as close as possible to 21 without going over it \n you dont know the dealers number of total cards \n you can stop if you think you are closer to 21 than the dealer \n')
import random
cardsplayer = 0
cardsbot = 0
randomvalue = 0
cardsplayer = cardsplayer + random.randint(5,10)
cardsplayer = cardsplayer + random.randint(5,10)
while 1 == 1:
    print(cardsplayer)
    ch = input(' [1] - to get a card (1 to 9) \n [2] - to bust the cards: ')
    if ch == '1':
        cardsplayer = cardsplayer + random.randint(1,9)
        if cardsplayer == 21:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU WON')
            exit()
        elif cardsplayer >= 22:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('YOU LOST')
            exit()
    elif ch == '2':
        print(cardsbot, ' - dealer', cardsplayer, ' - yours')
        if cardsplayer >= cardsbot:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)            
            input('you won')
            exit()
        else:
            print('you got', cardsplayer)
            print('and dealer got', cardsbot)
            input('you lost')
            exit()
    cardsbot = cardsbot + random.randint(1,9)
    if cardsbot == 21:
        print('you got', cardsplayer)
        print('and dealer got', cardsbot)
        input('YOU LOST')
        exit()
    elif cardsbot >= 22:
        print('you got', cardsplayer)
        print('and dealer got', cardsbot)
        input('YOU WON')
        exit()
