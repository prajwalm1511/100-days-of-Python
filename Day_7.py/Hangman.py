import random
# tODO - 1: Update the word list to use the 'word_list' from Hangman_words.py
from Hangman_art import HANGMANPICS
from Hangman_words import word_list
chance=0
# tODO-3 : Import the art from hangman_art.py and print it at the start if the game
chosen_word = random.choice(word_list)
print(chosen_word)
a=len(chosen_word)

placeholder="" # here first we define the type of placeholder
for i in range (1,a+1):
    
    placeholder +="_"
print(placeholder)

game_over=False
correct_letters=[]

while not game_over:
    
    guess = str(input("guess the letter: ")).lower()
    display=""

    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
    
        else:
            display+="_"
           
    print(display)        
    if guess not in chosen_word:
        chance += 1
        if chance==6:
            game_over=True
            print("You Loose")
                

                   
    
    if "_" not in display:
        game_over=True                                                   
        print("You win") 
    print(HANGMANPICS[chance])

    
   

    
