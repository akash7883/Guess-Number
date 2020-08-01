
#  its a simple Game
# you have to guess a number and this program will tell you if you are too low or too high or you win the game 

import random
gusess = 5

secrete_num = random.randint(1,10)
check_num = True


def is_number(): # validation for num in case user type a srring
     while check_num:
        try:
            global number
            number = int(input('enter a number : '))
            break
        except ValueError:
            print("please enter a number ")
            continue

def main(): 
    guess_count = 1
    while guess_count < gusess:
        is_number()


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
            guess_count += 1
            continue
if __name__ == "__main__":
    main()

        

    
