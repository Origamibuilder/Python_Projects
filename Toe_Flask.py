from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    #imports
    import time
    import webbrowser
    #Board setup
    board_list = []
        
    
    for i in range(1, 4):
        for j in range(1, 4):
            board_list.append(' ')

    board = '\n' + ' ' + str(board_list[0]) + ' |  ' + str(board_list[1]) + '  | ' + str(board_list[2]) + '\n -    -    -\n' + ' ' + str(board_list[3]) + ' |  ' + str(board_list[4]) + '  | ' + str(board_list[5]) + '\n -    -    -\n' + ' ' + str(board_list[6]) + ' |  ' + str(board_list[7]) + '  | ' + str(board_list[8]) + '\n'

  
        
    #Basic Outline
    print(board)
    print("Hello! This is Tic Tac Toe!")

    time.sleep(2) #sleeps 2 seconds

    print('\nEach slot from a specific column and row has a respective number assigned to it as you will see below.\n')

    time.sleep(2)

    for num in range(0, 9):
        board_list[num] = str(num + 1)

    board = '\n' + ' ' + str(board_list[0]) + ' |  ' + str(board_list[1]) + '  | ' + str(board_list[2]) + '\n -    -    -\n' + ' ' + str(board_list[3]) + ' |  ' + str(board_list[4]) + '  | ' + str(board_list[5]) + '\n -    -    -\n' + ' ' + str(board_list[6]) + ' |  ' + str(board_list[7]) + '  | ' + str(board_list[8]) + '\n'

    print(board)

    for num in range(0, 9): #resets board
        board_list[num] = ' '
    time.sleep(2)
    furtherInstructions = input('Would you like instructions on how to play or would you just like to play? Type "y" if you would like further instructions and anything else if not. ')


    if furtherInstructions == 'y':

        print('\nTo play a move when it is your turn, type in a number from 1-9 that is open to fill up that space. Try to get 3 in a row diagonally, horizontally, or vertically to win.\n')

        time.sleep(2)

        instructions = input('For more instructions on how to play, I can locate you to a site that is more in depth. Would you like me to? Type "y" if yes, type anything else if no. ')
        if instructions == 'y':
            print('\nHere you go.')
            time.sleep(.5)
            webbrowser.open('https://www.wikihow.com/Play-Tic-Tac-Toe')
    else:
        print('\nThank gosh there is actually a cultured person who knows how to play.')

        time.sleep(1)    

    name1 = input("\nHello player 1! Your are 'X's. What is your name? ")
    name2 = input("\nHello player 2! You are 'O's. What is your name? ")


    #Game Itself
    gameStatus = "Play"

    for num in range(0, 9):
        board_list[num] = ' ' #clears board
    
    while gameStatus != "Over":

        Player1Turn = input("\n" + str(name1) + ", it is your turn. Where would you like to play? ")

        while not Player1Turn.isdigit() or int(Player1Turn) not in range (1, 10) or board_list[int(Player1Turn) - 1] != ' ':
            while not Player1Turn.isdigit() or int(Player1Turn) not in range(1, 10):
                Player1Turn = input("Please type in an integer from 1-9. ")

            if board_list[int(Player1Turn) - 1] != ' ':
                Player1Turn = input("Please play a move in a space that is not already taken by an 'X' or 'O.' ")

   
        board_list[int(Player1Turn) - 1] = 'X'

        board = '\n' + ' ' + str(board_list[0]) + ' |  ' + str(board_list[1]) + '  | ' + str(board_list[2]) + '\n -    -    -\n' + ' ' + str(board_list[3]) + ' |  ' + str(board_list[4]) + '  | ' + str(board_list[5]) + '\n -    -    -\n' + ' ' + str(board_list[6]) + ' |  ' + str(board_list[7]) + '  | ' + str(board_list[8]) + '\n'


        print(board)

        #Checks to see if player 1 wins 
        for horizontal_wins_x in range(0, 9, 3):
            if board_list[horizontal_wins_x] == 'X' and board_list[horizontal_wins_x + 1] == 'X' and board_list[horizontal_wins_x + 2] == 'X':
                print('Game Over! ' + str(name1) + ', you win by getting three in a row horizontally!')
                gameStatus = 'Over'
                break
        for vertical_wins_x in range(0, 3):
            if board_list[vertical_wins_x] == 'X' and board_list[vertical_wins_x + 3] == 'X' and board_list[vertical_wins_x + 6] == 'X':
                print('Game Over! ' + str(name1) + ', you win by getting three in a row vertically!')
                gameStatus = 'Over'
                break
        if board_list[0] == 'X' and board_list[4] == 'X' and board_list[8] == 'X':
            print('Game Over! ' + str(name1) + ', you win by getting three in a row diagonally!')
            gameStatus = 'Over'
            break
        if board_list[2] == 'X' and board_list[4] == 'X' and board_list[6] == 'X':
            print('Game Over! ' + str(name1) + ', you win by getting three in a row diagonally!')
            gamesStatus = 'Over'
            break

        if gameStatus == 'Over':
            break 

        #Checks for a tie
        if board_list[0] != ' ' and board_list[1] != ' ' and board_list[2] != ' ' and board_list[3] != ' ' and board_list[4] != ' ' and board_list[5] != ' ' and board_list[6] != ' ' and board_list[7] != ' ' and board_list[8] != ' ':
            print("Game Over! All spaces were filled but no one got three in a row, so it's a tie!")
            gameStatus = 'Over'
            break

        if gameStatus == 'Over':
            break
    
        Player2Turn = input("\n" + str(name2) + ", it is your turn. Where would you like to play? ")

        while not Player2Turn.isdigit() or int(Player2Turn) not in range (1, 10) or board_list[int(Player2Turn) - 1] != ' ':
            while not Player2Turn.isdigit() or int(Player2Turn) not in range(1, 10):
                Player2Turn = input("Please type in an integer from 1-9. ")

            if board_list[int(Player2Turn) - 1] != ' ':
                    Player2Turn = input("Please play a move in a space that is not already taken by an 'X' or 'O.' ")

        board_list[int(Player2Turn) - 1] = 'O'

        board = '\n' + ' ' + str(board_list[0]) + ' |  ' + str(board_list[1]) + '  | ' + str(board_list[2]) + '\n -    -    -\n' + ' ' + str(board_list[3]) + ' |  ' + str(board_list[4]) + '  | ' + str(board_list[5]) + '\n -    -    -\n' + ' ' + str(board_list[6]) + ' |  ' + str(board_list[7]) + '  | ' + str(board_list[8]) + '\n'  

        print(board)

        #Checks to see if player 2 wins
        for horizontal_wins_o in range(0, 9, 3):
            if board_list[horizontal_wins_o] == 'O' and board_list[horizontal_wins_o + 1] == 'O' and board_list[horizontal_wins_o + 2] == 'O':
                print('Game Over! ' + str(name2) + ', you win by getting 3 in a row horizontally!')
                gameStatus = 'Over'
                break
        for vertical_wins_o in range(0, 3):
            if board_list[vertical_wins_o] == 'O' and board_list[vertical_wins_o + 3] == 'O' and board_list[vertical_wins_o + 6] == 'O':
                print('Game Over! ' + str(name2) + ', you win by getting three in a row vertically!')
                gameStatus = 'Over'
                break
        if board_list[0] == 'O' and board_list[4] == 'O' and board_list[8] == 'O':
            print('Game Over! ' + str(name2) + ', you win by getting three in a row diagonally!')
            gameStatus = 'Over'
            break
        if board_list[2] == 'O' and board_list[4] == 'O' and board_list[6] == 'O':
            print('Game Over! ' + str(name2) + ', you win by getting three in a row diagonally!')
            gameStatus = 'Over'
            break


if __name__ == '__main__':
    app.run(debug = True)
    

                             
