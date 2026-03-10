# hangman #

#Step 1
#to check if the guessed letter is in the word or not
import random
word_list =['aardvark','baboon','camel']
chosen_word = random.choice(word_list)
print(chosen_word)
guess=str(input("Guess the letter: ")).lower()

for i in chosen_word:
    
    if i==guess:
        print("right")
    else:
        print("wrong")

#step 2 # applying place holders
a=len(chosen_word)
print(chosen_word)
placeholder="" # here first we define the type of placeholder
for i in range (1,a+1):
    
    placeholder +="_" 

print(placeholder)
c=""
for i in chosen_word:
    if guess==i:
        c+=i
    else:
        d="_"
        c+=d
print(c)

# step 3 Giving repetitve guesses

for i in c:
    if i=='_':
        guess=str(input("Guess the letter: ")).lower()
        c=""
        for i in chosen_word:
            if guess==i:
                c+=i
            else:
                d="_ "
                c+=d
        p=c
print(p)
    


    

    
    


