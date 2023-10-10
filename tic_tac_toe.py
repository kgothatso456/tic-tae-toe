import random

def tic_tac_toe():

    print("Welcome to Tic-Tac-Toe")

    a = '1'
    b = '2'
    c = '3'
    d = '4'
    e = '5'
    f = '6'
    g = '7'
    h = '8'
    i = '9'
    nums = [i*1 for i in range(1, 10)]

    
    all_choices = []

    # Tic Tac Toe drawing board
    def draw(a, b, c, d, e, f, g, h, i):
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   {}   |   {}   |   {}   |'. format(a,b,c))
        print('|       |       |       |')
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   {}   |   {}   |   {}   |'.format(d,e,f))
        print('|       |       |       |')
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   {}   |   {}   |   {}   |'.format(g,h,i))
        print('|       |       |       |')
        print('+-------+-------+-------+')


    draw(a, b, c, d, e, f, g, h, i)

    # Once all the spaces on the board have been filled display game over
    if len(all_choices) == 9:
        print("Game Over")


    while len(all_choices) != 9:
        user = input("Enter your move: ")

        # While loop checks the user input and places the user choice on the tic tac toe board
        while True:
            if user.isdigit() and int(user)>0 and int(user)<10 and int(user) not in all_choices:

                if int(user) == 1:
                    a = "O"

                elif int(user) == 2:
                    b = "O"
                    
                elif int(user) == 3:
                    c = "O"
                    
                elif int(user) == 4:
                    d = "O"
                    
                elif int(user) == 5:
                    e = "O"
                    
                elif int(user) == 6:
                    f = "O"
                    
                elif int(user) == 7:
                    g = "O"
                    
                elif int(user) == 8:
                    h = "O"
                    
                elif int(user) == 9:
                    i = "O"

                break

            else:
                print("Enter a valid number from 1 to 9.")
                user = input("Enter your move: ")

        
        all_choices.append(int(user))

        # computer choice choosen randomly
        computer_choice = random.choice(nums)


        # While loop to place the computer choice on the tic tae toe board
        while True:
            if computer_choice not in all_choices: 
                all_choices.append(computer_choice)
                if int(computer_choice) == 1:
                    a = "X"
                elif int(computer_choice) == 2:
                    b = "X"
                elif int(computer_choice) == 3:
                    c = "X"
                elif int(computer_choice) == 4:
                    d = "X"
                elif int(computer_choice) == 5:
                    e = "X"
                elif int(computer_choice) == 6:
                    f = "X"
                elif int(computer_choice) == 7:
                    g = "X"
                elif int(computer_choice) == 8:
                    h = "X"
                elif int(computer_choice) == 9:
                    i = "X"
                break
            else:
                computer_choice = random.choice(nums)

        # after both the user and computer have placed their move, display the board to the user
        draw(a, b, c, d, e, f, g, h, i)

        # print(all_choices)

        # Determine game win

        #win by rows
        if a == 'O' and b == 'O' and c == 'O':
            print("You Win!")
            return
        elif a == 'X' and b == 'X' and c == 'X':
            print("Computer Wins!")
            return
        elif d == 'O' and e == 'O' and f == 'O':
            print("You Win!")
            return
        elif d == 'X' and e == 'X' and f == 'X':
            print("Computer Wins!")
            return
        elif g == 'O' and h == 'O' and i == 'O':
            print("You Win!")
            return
        elif g == 'X' and h == 'X' and i == 'X':
            print("Computer Wins!")
            return
        
        #win across
        elif a == 'O' and e == 'O' and i == 'O':
            print("You Win!")
            return
        elif a == 'X' and e == 'X' and i == 'X':
            print("Computer Wins!")
            return
        elif c == 'O' and e == 'O' and g == 'O':
            print("You Win!")
            return
        elif c == 'X' and e == 'X' and g == 'X':
            print("Computer Wins!")
            return
        
        #win by columns
        elif a == 'O' and d == 'O' and g == 'O':
            print("You Win!")
            return
        elif a == 'X' and d == 'X' and g == 'X':
            print("Computer Wins!")
            return
        elif b == 'O' and e == 'O' and h == 'O':
            print("You Win!")
            return
        elif b == 'X' and e == 'X' and h == 'X':
            print("Computer Wins!")
            return
        elif c == 'O' and f == 'O' and i == 'O':
            print("You Win!")
            return
        elif c == 'X' and f == 'X' and i == 'X':
            print("Computer Wins!")
            return

# While loop to loop the game until it ends and gives the user the option to play again

while True:
    tic_tac_toe()
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break