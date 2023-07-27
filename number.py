import random

play_again = True

while play_again:
    print("Welcome to my guessing game")
    level = input("Choose level. Type 'easy' or 'hard' ")
    if level == 'easy':
        number_of_guesses = 5
    elif level == 'hard':
        number_of_guesses = 10
    else:
        break
    
    print(f"you have {number_of_guesses} attempts remaining to guess the number.")
    
    play_game = True
    
    while play_game and number_of_guesses !=0:
        answer = random.randint(1,100)
        guess = int(input("Make a guess:"))
        if guess != answer:
            number_of_guesses -= 1
            if guess > answer:
                print(f'{guess} is too high. Guess again.')
                print(f'you have {number_of_guesses} attempts remaining to guess.')
            elif guess < answer:
                print(f'{guess} is too low. Guess again.')
                print(f'you have {number_of_guesses} attempts remaining to guess.')
            
        else:
            play_game = False
            
    if guess == answer:
        print(f'you guessed the number! It was {answer}. You win!')
    else:
        print(f'You ran out of guesses. The number was {answer}. you lose!')
        
    try_again = input("Would you like to play again? 'y' or 'n':")
    if try_again != 'y':
        play_again = False    
    
        
        