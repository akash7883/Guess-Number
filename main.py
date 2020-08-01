
#  its a simple Game
# you have to guess a number and this program will tell you if you are too low or too high or you win the game 

import random
gusess = 5
guess_count =1
secrete_num = random.randint(1,10)
check_num = True

while guess_count < gusess:

    while check_num:
        try:
            number = int(input('enter a number : '))
            break
        except ValueError:
            print("please enter a number ")
            continue

    if number < secrete_num:
        print("to low")
        print(f'you left with {gusess -guess_count} ')
        print(secrete_num)
        guess_count += 1
        continue
    elif number == secrete_num:
        print("you won congratulations")
        break
    elif number > secrete_num:
        print("you are to high")
        print(f'you left with {gusess -guess_count} ')
        print(secrete_num)
        guess_count+= 1
        continue
        

    
