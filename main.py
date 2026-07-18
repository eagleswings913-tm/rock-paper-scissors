import random

# Rock, Paper, Scissors Game

# Rock wins against Scissors
# Scissors wins against Paper
# Paper wins against Rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

game_stats = {"games": 0, "ties": 0, "user_wins": 0, "computer_wins": 0}

continue_play = True

def random_number():
    return random.randint(0, 2)

while continue_play:
    game_stats["games"] += 1

    user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n'))

    if 0 <= user_choice <= 2:

        print(game_images[user_choice])

        computer_choice = random_number()
        print ('Computer chose: ', computer_choice)
        print(game_images[computer_choice])

        if user_choice == computer_choice:
            print("It's a draw!")
            game_stats["ties"] += 1
        else:
            if user_choice == 0:
                if computer_choice == 1:
                    print ("Computer wins")
                    game_stats["computer_wins"] += 1
                else:
                    print ("You win")
                    game_stats["user_wins"] += 1
            elif user_choice == 1:
                if computer_choice == 0:
                    print("You win!")
                    game_stats["user_wins"] += 1
                else:
                    print("Computer wins!")
                    game_stats["computer_wins"] += 1
            elif user_choice == 2:
                if computer_choice == 0:
                    print("Computer wins!")
                    game_stats["computer_wins"] += 1
                else:
                    print("You win!")
                    game_stats["user_wins"] += 1
    else:
        print("Invalid choice: Please enter 0 for Rock, 1 for Paper, 2 for Scissors")

    if (input('Do you want to play again? (Y/n): ').lower()  or "y") == 'n':
        continue_play = False

print(f"You played {game_stats['games']} times!")
print(f"You tied {game_stats['ties']} times!")
print(f"You won {game_stats['user_wins']} times!")
print(f"Computer won {game_stats['computer_wins']} times!")