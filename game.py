import random

# easy stage
easy_guess_limit = 6
easy_result = random.randint(1, 10)

# medium stage
medium_guess_limit = 4
medium_result = random.randint(1, 20)

# hard stage
hard_guess_limit = 3
hard_result = random.randint(1, 50)



guess = ""
out_of_guesses = False
guess_count = 0

start = str(input("please ener your prefered game level, (E for easy), (M for medium), (H for hard): "))

if start  == 'E' or start  == 'e'  :  #for stage
    while guess != easy_result and not(out_of_guesses):
        if guess_count < easy_guess_limit:
            guess = int(input('please enter your guess here: '))
            guess_count += 1
            if guess != easy_result:
                print(f'That was wrong, you have used {guess_count} guess, {6 - guess_count } left to play')
            else:
                pass
        else:
            out_of_guesses = True

    if out_of_guesses:
        print('Out of guesses, Game over')
    else:
        print('you got it right')
elif start == 'M' or start  == 'm' : #for medium stage
    while guess != medium_result and not(out_of_guesses):
        if guess_count < medium_guess_limit:
            guess = int(input('please enter your guess here: '))
            guess_count += 1
            if guess != easy_result:
                print(f'That was wrong, you have used {guess_count} guess, {4 - guess_count } left to play')
            else:
                pass
        else:
            out_of_guesses = True

    if out_of_guesses:
        print('Out of guesses, Game over')
    else:
        print('you got it right')
elif start =='H' or start  == 'h' : #for hard stage
    while guess != hard_result and not(out_of_guesses):
        if guess_count < hard_guess_limit:
            guess = int(input('please enter your guess here: '))
            guess_count += 1
            if guess != easy_result:
                print(f'That was wrong, you have used {guess_count} guess, {3 - guess_count } left to play')
            else:
                pass
        else:
            out_of_guesses = True

    if out_of_guesses:
        print('Out of guesses, Game over')
    else:
        print('you got it right')





    
 