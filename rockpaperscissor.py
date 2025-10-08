print("Welcome to the Game!!")
Flag = True

while Flag == True:
    print('''Here are some available choice for you
        Rock
        Paper
        Scissor
        ''')
    user = input("Enter your Choice: ")
    collection = ['rock', 'paper', 'scissor']

    import random
    computer = random.choice(collection)

    if (user == 'rock' and computer == 'paper') or (user == 'paper' and computer == 'scissor') or (user == 'scissor' and computer == 'rock'):
        print("Computer Wins!!")
    elif (user == 'rock' and computer == 'scissor') or (user == 'paper' and computer == 'rock') or (user == 'scissor' and computer == 'paper'):
        print("You Won!!")
    elif user == computer:
        print("Tie!!")
    else:
        print("Wrong Input!!")
        Flag = False
    print('''Would you like to play again?,
          if yes, press 1
          if no, press 0''')
    user = int(input("Enter Choice: "))
    if user == 0:
        Flag = False
print("Thank you!!, see you")
