#entry to the game
import random
print('Hello! Lets play rock, paper, scissors.')
#strat of a new round of the game
def new_game():
    print("How many wins will determine the winner?")

    while True:
        try:
            enter_a_number = int(input("Number of wins: "))
            break
        except ValueError:
            print("You have to choose a number")
    print("Okay, whoever has " + str(enter_a_number) + " wins first wins it all!")
    print('Lets play! (Enter "R" for rock,"P" for paper and "S" for scissors)')
    computer_wins = 0
    player_wins = 0
    draws = 0
    #counter function that will show all results
    def counter():
        print("My wins: " + str(computer_wins))
        print("Your wins: " + str(player_wins))
        print("Draws: " + str(draws))
    #rules for onr round of the game
    def one_game():
        #variables that will be needed in the game
        nonlocal computer_wins
        nonlocal player_wins
        nonlocal draws
        #generating the computer's play
        computer = random.randint(1, 4)
        computer_played = ""
        #making the computer and the player have the same answers
        if computer == 1:
            computer_played = "ROCK"
        elif computer_played == 2:
            computer_played = "PAPER"
        else:
            computer_played = "SCISSORS"
        # testing if the player gives the right answer
        while True:
            try:
                player = str(input("You play: "))
                if player == 'R' or player == 'P' or player == 'S':
                    break

            except ValueError:
                print('You have to choose "R", "P" or "S"')
        # making the computer and the player have the same answers
        if player == "R":
            player_played = "ROCK"
        elif player == "P":
            player_played = "PAPER"
        else:
            player_played = "SCISSORS"

        print("I play " + computer_played + " , you played " + player_played)
        # comparing the plays of the computer and the player
        if computer_played == player_played:
            draws += 1
            print("Its a draw")
        else:
            if computer_played == "ROCK" and player_played == "PAPER":
                player_wins += 1
                print('You win!')
            elif computer_played == "ROCK" and player_played == "SCISSORS":
                computer_wins += 1
                print("I win!")
            elif computer_played == "PAPER" and player_played == "ROCK":
                computer_wins += 1
                print("I win!")
            elif computer_played == "PAPER" and player_played == "SCISSORS":
                player_wins += 1
                print('You win!')
            elif computer_played == "SCISSORS" and player_played == "ROCK":
                player_wins += 1
                print('You win!')
            elif computer_played == "SCISSORS" and player_played == "PAPER":
                computer_wins += 1
                print("I win!")
    #processing results of the game
    while True:
        if computer_wins >= enter_a_number or player_wins >= enter_a_number:
            break
        else:
            one_game()
    if computer_wins > player_wins:
        print("You lose.")
        print(counter())
    else:
        print("YOU ARE THE WINNER!")
        print(counter())
    print("Do you wish to play another game?")
    while True:
        try:
            player = str(input('Another game?("Y" for yes ans "N" or no): '))
            if player == 'Y' or player == 'N':
                break

        except ValueError:
            print('You have to choose "Y" or "N"')
    if player == 'Y':
        new_game()
    else:
        print('It was fun playing. See you soon!')

new_game()




