import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word=get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print("You have " ,lives,' left and you have used letters: ', ' '.join(used_letters))
        #getting user input
        user_letter = input('Guess a letter: ').upper()
         
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in the word. Try',random.choice(list(word_letters)))   
          
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
            
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')
        
if __name__ == '__main__':
    hangman()