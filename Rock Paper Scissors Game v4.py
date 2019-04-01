from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2
# User is playing with the Computer (Mini AI)

print("You'll be playing these game with the Computer/Robot")

# Users are to pick from the following options
print('Choose from the three (3) options below to play this games')
def display_header():
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

def pick_computer_move():
    rand_num = randint(0,2)
    if (rand_num == 0):
        move = 'rock'
    elif (rand_num == 1):
        move = 'paper'
    else:
         move = 'scissors'
    print('Computer plays {}'.format(move))
    return move

def calculate_winner(x, computer):
    global player_wins
    global computer_wins
    if x == computer:
            print('Its a Tie!')
    elif x == 'rock':
        if computer == 'paper':
            print('Computer wins :( ')
            computer_wins += 1
        else:
            print('Player wins')
        player_wins += 1
    elif x == 'paper':
        if computer == 'rock':
            print('Player wins')
            player_wins += 1
        else:
            print('Computer wins')
            computer_wins += 1
    elif x == 'scissors':
        if computer == 'paper':
            print('Player wins')
            computer_wins += 1
        else:
            print('Computer wins')
            player_wins += 1

    #If user Enters Anything other than The options giving
    else:
        print('Please enter a valid move!')

def start_game(winner_score):
    while player_wins < winning_score and computer_wins < winning_score:
        display_header()

        x = input('Player 1, make your Choice: ').lower()
        if x == 'quit' or x == 'q':
            break

        computer = pick_computer_move()
        calculate_winner(x, computer)

def display_winner():
    if player_wins > computer_wins:
        print('Congrats, You Won!')
    elif player_wins == computer_wins:
        print('Its a Tie')
    else:
        print('Oh! No. The Computer Won!')

start_game(3)
display_winner()

#print(f'Final Scores... Player Score: {player_wins}, Computer Wins: {computer_wins}')

