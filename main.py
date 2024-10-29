"""
Rock Paper Scissors Game
-------------------------------------------------------------
"""

import random
import os

# Constants
CHOICES = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
VALID_RESPONSES = ['yes', 'no', 'y', 'n']
RESULTS = {
    ('R', 'S'): 'Rock crushes Scissors! You win!',
    ('S', 'P'): 'Scissors cut Paper! You win!',
    ('P', 'R'): 'Paper covers Rock! You win!',
    ('S', 'R'): 'Rock crushes Scissors! I win!',
    ('P', 'S'): 'Scissors cut Paper! I win!',
    ('R', 'P'): 'Paper covers Rock! I win!'
}

# Functions
def clear_screen():
    """Clear the screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_score(user_score, computer_score):
    """Display the current score."""
    print(f'Score - You: {user_score}, Computer: {computer_score}\n')

def check_play_status():
    """Check if the user wants to play again."""
    while True:
        response = input('Do you wish to play again? (Yes or No): ').strip().lower()
        if response in VALID_RESPONSES:
            return response in ['yes', 'y']
        print('Invalid response. Please enter Yes or No.')

def get_user_choice():
    """Prompt the user to choose Rock, Paper, or Scissors."""
    while True:
        user_choice = input('Choose your weapon [R]ock, [P]aper, or [S]cissors: ').strip().upper()
        if user_choice in CHOICES:
            print(f'You chose: {CHOICES[user_choice]}')
            return user_choice
        print('Invalid choice. Please choose [R]ock, [P]aper, or [S]cissors.')

def play_rps():
    """Play the Rock Paper Scissors game."""
    user_score, computer_score = 0, 0

    while True:
        clear_screen()
        print('\nRock, Paper, Scissors - Shoot!')

        user_choice = get_user_choice()
        computer_choice = random.choice(list(CHOICES.keys()))
        print(f'I chose: {CHOICES[computer_choice]}')

        if user_choice == computer_choice:
            print("It's a Tie!")
        else:
            result_message = RESULTS.get((user_choice, computer_choice))
            if result_message and 'You win' in result_message:
                user_score += 1
            else:
                computer_score += 1
            print(result_message)

        display_score(user_score, computer_score)

        # Ask if the player wants to continue
        if not check_play_status():
            clear_screen()
            print('Thanks for playing!')
            display_score(user_score, computer_score)
            break

if __name__ == '__main__':
    play_rps()
