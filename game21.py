kolada = [6,7,8,9,10,11] * 4

import random
random.shuffle(kolada)

print("пограємо в 21!!!")

count = 0
while True:
     choice = input("Будете брати карту??? tak \ nie \n ")
     if choice == 'nie':
         print("дякую)")
         break
     if choice == 'tak':
         current = kolada.pop()
         print("Вам попалась карта %d" %current)
         count += current
         if count > 21:
             print("Ви програли %d очків" %count)
             break
         elif count == 21:
             print("У вас 21 очко,Поздоровляю!!!")
             break
         else:
             print("У вас %d очків" %count)
     elif choice == 'n':
         print("У вас %d очків і ви закінчили гру!!!" %count)
         break


print("Дякую за ігру")


