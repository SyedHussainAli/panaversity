import random

def rock_paper_sissor():
    choices = ['rock', 'paper', 'sissor']
    computer_choice = random.choice(choices)
    user_choice = input('Rock, Paper, or Sissor? ').lower()     
    if user_choice not in choices:
        print('Invalid choice. Please choose rock, paper, or sissor.')
        return rock_paper_sissor()
    print(f'Computer chose {computer_choice}.')
    if computer_choice == user_choice:
        print('It\'s a tie!')
    elif computer_choice == 'rock' and user_choice == 'sissor':
        print('Computer wins!')
    elif computer_choice == 'paper' and user_choice == 'rock':
        print('Computer wins!')
    elif computer_choice == 'sissor' and user_choice == 'paper':
        print('Computer wins!')
    else:
        print('You win!')
        
if __name__ == '__main__':
    rock_paper_sissor()