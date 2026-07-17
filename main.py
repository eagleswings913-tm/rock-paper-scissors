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

def print_choice(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)

def random_number():
    return random.randint(0, 2)

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n'))
print_choice(user_choice)

computer_choice = random_number()
print ('Computer chose: ', computer_choice)
print_choice(computer_choice)

if user_choice == 0:
    if computer_choice == 0:
        print("Tie")
    elif computer_choice == 1:
        print ("Computer wins")
    else:
        print ("You win")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("Tie")
    else:
        print("Computer wins!")
elif user_choice == 2:
    if computer_choice == 0:
        print("Computer wins!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("Tie")
else:
    print("Invalid choice: Please enter 0 for Rock, 1 for Paper, 2 for Scissors")
