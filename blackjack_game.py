koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)
print('Пограємо в очко!')
bill = 0
true= 3

while true == 3:
    choice = input('Будете брати карту? так/ні\n')
    if choice == 'так':
        account = koloda.pop()
        print('Вам попалась карта з властивістю %d' %account)
        bill += account
        if bill > 21:
            print('Вибачте, Ви програли')
            true = 4
        elif bill == 21:
            print('Вітаємо з перемогою!')
            true = 4
        else:
            print(' У Вас %d очків' %bill)
            true = 3
    else:
        print('Ну як хочете')
        break
    while true == 4:
        exit = input("Ви хочете продовжити? так/ні\n ")
        if exit == 'так':
            true = 3
            bill = 0
            break
        elif exit == 'ні':
        	    print('До зустрічі !')
        	    break
