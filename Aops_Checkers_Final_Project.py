from tkinter import *

class CheckerSquare(Canvas):
    '''Creates New Checker Square'''

    def __init__(self, master, color_type, r, c):
        '''CheckerSquare(master, color_type, r, c)
        creates a new blank Checker square at coordinate (r, c)'''
        # create and place the widget
        Canvas.__init__(self, master, width=50, height=50, bg=color_type)

        #Only green tiles work
        if color_type == 'dark green':
            self.functions = True
        elif color_type == 'blanched almond':
            self.functions = False
  
        self.grid(row=r, column=c)

        # set the coords
        self.row = r

        self.column = c
        
        self.position = (r, c)

        #No checker in checker square right now
        self.checker = None
        
        # bind button click to placing a piece
        self.bind('<Button-1>', master.get_click)

    def get_row(self):
        '''CheckerSquare.get_row() -> str
        returns the row coord of the checker square'''

        return self.row

    def get_column(self):
        '''CheckerSquare.get_column() -> str
        returns the column coord of the checker square'''

        return self.column

    def get_position(self):
        '''CheckerSquare.get_position() -> (int, int)
        returns (row, column) of square'''

        return self.position

    def does_function(self):
        '''CheckerSquare.does_function() -> Boolean
        returns whether square is actually functionable
        (if a square is white, it does not function)'''
        
        return self.functions

    def place_checker(self, checker):
        '''CheckerSquare.place_checker(checker)
        puts checker down on checker square'''

        #Puts checker down 
        self.checker = checker

        #Deletes all checkers in the square
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)

        #Creates oval that is the checker's color
        self.create_oval(10, 10, 44, 44, fill = checker.get_color())

        #If the checker is a king, update the display of the checker
        if checker.is_king():
            self.create_text(27, 28, text='K', font=('Arial', 18, 'bold'), fill='gold')

        #There is a checker
        self.is_checker = True

        #Sets the coord of the checker to a the position of the checker square
        checker.set_coord(self.get_position())
        
    def remove_checker(self):
        '''CheckerSquare.place_checker()
        Removes checker from checker square'''

        #Finds all checkers and deletes them
        ovalList = self.find_all()

        for oval in ovalList:
            self.delete(oval)

        self.is_checker = False

        self.checker = None

    def has_checker(self):
        '''CheckerSquare.place_checker() -> Boolean
        returns whether there is checker on checker board or not'''

        return self.is_checker

    def get_checker(self):
        '''CheckerSquare.get_checker()
        returns the checker that is on this checker board'''
    
        return self.checker

class Checker:
    '''Creates new Checker'''

    def __init__(self, color, coord):
        '''Checker(color, coord)
        creates a new Checker and sets its coord to coord'''

        #Sets color, initallizes them to not being a king
        self.color = color

        self.king = False

        #Sets coord to coord
        self.coord = coord

        #Checker is not initally a king
        self.initially_king = False

    def is_king(self):
        '''Checker.is_king() -> Boolean
        Returns whether the checker is a king'''

        return self.king

    def promote_king(self):
        '''Checker.promote_king() 
        Promotes checker to a king'''

        self.king = True

    def get_color(self):
        '''Checker.get_color() -> str
        returns the color of the checker'''

        return self.color

    def moves_forward(self):
        '''Checker.moves_forward() -> Boolean
        returns whether the checker moves forward (white)
        or if the checker moves backwards (red)'''

        if self.get_color() == 'white':
            return True
        else:
            return False

    def set_coord(self, coord):
        '''Checker.set_coord(coord)
        sets the coordinate of the Checker to a coord'''
        
        self.coord = coord

    def get_position(self):
        '''Checker.get_position() -> str
        returns the position of the checker'''

        return self.coord

class Play_Checkers(Frame):
    '''Plays Checkers Game'''

    def __init__(self, master):
        '''Play_Checkers(master)
        creates a Checkers Board in starting position'''

        #Imports frame init
        Frame.__init__(self,master,bg='white')

        #Makes grid
        self.grid()

        self.board = {}  # dict to store position
        self.checker_list = []
        # create opening position
        for row in range(8):
            for column in range(8):
                coords = (row, column)
                if (row + column) % 2 == 0:
                    color = 'blanched almond'
                else:
                    color = 'dark green'

                checker = None
    
                #Sets inital areas where the checkers are
                if color == 'dark green':
                    if row in range(5, 8, 1):
                        self.checker_list.append(Checker('white', coords))
                    elif row in range(3):
                        self.checker_list.append(Checker('red', coords))
                        
                self.board[coords] = CheckerSquare(self, color, row, column)

        self.currentPlayer = 1  # player 1 starts

        self.click_num = 0 #No clicks on the board

        self.start_coord = None #Inital checker clicked

        self.end_coord = None #Checker that has not been clicked 

        self.capture = False #No capture is available
        
        #Turn label
        self.turn_label = Label(self, text = 'Turn:', font = ('Arial', 15), bg = 'white')

        self.turn_label.grid(row = 8, column = 1)
        
        #Creates label to changes based off of turn
        self.play_color_label = CheckerSquare(self, 'light gray', 8, 2)

        self.play_color_label.grid(row  = 8, column = 2)

        self.play_color_label.unbind('<Button-1>')

        #Checker that changes
        self.display_checker = Checker('red', (8, 2))

        self.play_color_label.place_checker(self.display_checker)

        #Label that commentates during the game
        self.gameLabel = Label(self, text = '', font = ('Arial', 12),  bg = 'white')

        self.gameLabel.grid(row = 8,column = 3, columnspan = 5)

        self.specific_checker_square = None
    
        #Updates inital display

        self.update_display()

        #Plays checkers
        
        self.play_checkers()
        
    def get_piece(self, coords):
        '''Player_Checkers.get_piece(coords) -> CheckerBoard()
        returns CheckerBoard'''
        
        return self.board[coords]

    def get_player(self):
        '''Play_Checkers.get_player() -> int
        returns the current player num'''

        return self.currentPlayer
    
    def update_display(self):
        '''Play_Checkers.update_display()
        Updates board display'''

        #For every checker square coord in self.board
        for square in self.board:
            #Remove all checkers and make their highlight background white
            self.board[square].remove_checker()
            self.board[square]['highlightbackground'] = 'white'

            #If checker is on checker_square place checker there
            for checker in self.checker_list:
                if self.board[square].get_position() == checker.get_position():
                    self.board[square].place_checker(checker)
                    
    def get_click(self, event):
        '''Play_Checkers.get_click(event)
        Gets click input and updates board display off of that'''

        #Coords is where user clicked
        coords = event.widget.get_position()

        #If the area clicked does not function do not do anything
        if not self.board[coords].does_function():
            return

        #If the click number is 0 and no checker is clicked do not do anything
        if self.click_num == 0:
            if not self.board[coords].has_checker():
                return

        #If the click number is 1 and the user clicks another checker as their
        #second turn end the turn
        if self.click_num == 1:
            if self.board[coords].has_checker():
                for square in self.board.values():
                    square['highlightbackground'] = 'white'
                self.board[coords]['highlightbackground'] = 'black'
                self.start_coord = coords
                return

        #Increment the click num
        self.click_num += 1

        #Highlight the checker square clicked in black
        self.board[coords]['highlightbackground'] = 'black'

        #Set the inital coords of the checker square to the area where the board
        #was clicked
        if self.click_num == 1:
            self.start_coord = coords
            return

        #If second place if clicked
        elif self.click_num == 2:

            #Second area clicked gets updated
            self.end_coord = coords

            #Checks to see if the turn is legal
            response = self.is_turn_legal(self.start_coord, self.end_coord)

            #If the turn is legal but it is not capturing anything
            if response and not self.capture:
                #Go forward and reset/ end turn
                self.play_move()
                self.board[self.start_coord]['highlightbackground'] = 'white'
                self.start_coord = coords
                self.end_coords = None
                self.board[coords]['highlightbackground'] = 'black'

                self.end_turn()  # Check if turn should end or continue
                return

            #If turn is legal and something is getting captured
            elif response and self.capture:

                #No capture done
                self.capture = False

                #Checks if the checker is initally a king
                king = self.board[self.start_coord].get_checker().is_king()

                #Captures other checker and moves
                self.do_capture()

                #If the checker was not initally a king and now is end turn and stop
                if self.board[coords].get_checker().is_king() and king == False:
                    
                    self.end_turn()
                    return

                #Specified checker square that the user is forced to click
                #if user captures checker and more captures are needed
                self.specific_checker_square = self.board[coords]

                #Checks if the turn should be ended
                end = self.check_turn_end()  # Check if turn should end or continue

                #If the turn should not be ended
                if not end:
                    #Forces user to continue jumping with the same square
                    #and highlights that required square
                    self.click_num == 1
                    self.end_coord = None
                    self.capture = False
                    self.board[coords]['highlightbackground'] = 'black'
                    self.start_coord = coords
                    self.gameLabel['text'] = 'Must continue jump!'
                else:
                    return

            #Otherwise   
            else:
                #Unhighlights square background  
                self.board[coords]['highlightbackground'] = 'white'

            #Initializes in case another turn is going to played
            self.click_num = 1
            self.end_coord = None
            self.capture = False

    def is_turn_legal(self, start_coord, end_coord):
        '''Play_Checkers.is_turn_legal(start_coord, end_coord) -> Boolean
        Returns whether it is a legal move for the checker on the start coord
        to go to the checker on the end coord'''

        #If end coord or start coord are out of bounds stop and return False
        if end_coord[0] < 0 or end_coord[0] > 7 or end_coord[1] < 0 or end_coord[1] > 7:
            return False
        
        if start_coord[0] < 0 or start_coord[0] > 7 or start_coord[1] < 0 or start_coord[1] > 7:
            return False

        #Checks to make sure that there is a checker at the inital coord
        for checker in self.checker_list:
            if checker.get_position() == start_coord:
                correspond_checker = checker
                is_checker = True
                break
            is_checker = False
    
        if not is_checker:
            return False

        #Gets checkers color
        color = correspond_checker.get_color()

        #Gets opposite sides color
        if color == 'white':
            opp_color = 'red'
        else:
            opp_color = 'white'

        #If the checker is a king
        if correspond_checker.is_king():
           
            #If the surrounding tiles are open and that is the end coord inputted
            #return True 
            for row_change in range(-1, 2, 2):
                for column_change in range(-1, 2, 2):
                    row_check = start_coord[0] + row_change

                    column_check = start_coord[1] + column_change

                    #Makes sure that it is not out of bounds
                    if row_check < 0 or row_check > 7 or column_check < 0 or column_check > 7:
                        continue
                    
                    coord = (row_check, column_check)

                    if end_coord == coord:
                        return True

            #If the surrounding tiles that are two spaces away and that is the end_coord
            #inputted return True and capture the checker
            for row_change in range(-2, 3, 4):
                for column_change in range(-2, 3, 4):
                    row_check = start_coord[0] + row_change

                    column_check = start_coord[1] + column_change

                    #Checks to make sure that it does not pass the boundary
                    if row_check < 0 or row_check > 7 or column_check < 0 or column_check > 7:
                        continue

                    if self.board[(row_check, column_check)].has_checker():
                        continue

                    coord = (row_check, column_check)

                    in_between_coord = (start_coord[0] + (row_change // 2), start_coord[1] + (column_change // 2))

                    #If the in_between_coord is a checker of the opposite color
                    for checker in self.checker_list:
                        if checker.get_position() == in_between_coord:
                            between_checker = checker
                            leave = False
                            break
                    
                        leave = True
                        
                    if leave:
                        continue
                    
                    if end_coord == coord:
                        if between_checker.get_color() == opp_color:
                            self.capture = True
                            return True
            
            return False

        #If the checker is not a king and white
        elif correspond_checker.moves_forward():
            
            #More limited boundary because it is not king
            for column_change in range(-1, 2, 2):
                row_check = start_coord[0] - 1

                column_check = start_coord[1] + column_change

                #Checks for out of bounds
                if row_check < 0 or column_check < 0 or column_check > 7:
                    continue

                coord = (row_check, column_check)

                if end_coord == coord:
                    return True

            #More limited boundary because it is not king
            for column_change in range(-2, 3, 4):
                row_check = start_coord[0] - 2

                column_check = start_coord[1] + column_change

                #If checker is out of bounds
                if row_check < 0 or row_check > 7 or column_check < 0 or column_check > 7:
                    continue

                if self.board[(row_check, column_check)].has_checker():
                        continue

                coord = (row_check, column_check)

                in_between_coord = (start_coord[0] - 1, start_coord[1] + (column_change / 2))

                for checker in self.checker_list:
                    if checker.get_position() == in_between_coord:
                        between_checker = checker
                        leave = False
                        break
                    
                    leave = True
                        
                if leave:
                    continue
                    
                if end_coord == coord:
                    #If the in between is the opposite color
                    if between_checker.get_color() == opp_color:
                        self.capture = True
                        return True
            
            return False            
            
        #If the checker is not a king and red
        else:
            
            for column_change in range(-1, 2, 2):
                row_check = start_coord[0] + 1

                column_check = start_coord[1] + column_change

                if row_check > 7 or column_check < 0 or column_check > 7:
                    continue

                coord = (row_check, column_check)

                if end_coord == coord:
                    return True

            
            for column_change in range(-2, 3, 4):
                row_check = start_coord[0] + 2

                column_check = start_coord[1] + column_change

                if row_check < 0 or row_check > 7 or column_check < 0 or column_check > 7:
                    continue

                if self.board[(row_check, column_check)].has_checker():
                        continue

                coord = (row_check, column_check)

                in_between_coord = (start_coord[0] + 1, start_coord[1] + (column_change / 2))

                for checker in self.checker_list:
                    if checker.get_position() == in_between_coord:
                        between_checker = checker
                        leave = False
                        break
                    
                    leave = True
                        
                if leave:
                    continue
                    
                if end_coord == coord:
                    if between_checker.get_color() == opp_color:
                        self.capture = True
                        return True
            

            return False
        
    def play_move(self):
        '''Play_Checkers.play_move()
        Plays move from checker to area'''

        #Finds checker that has the coord
        for checker in self.checker_list:
            if checker.get_position() == self.start_coord:
                correspond_checker = checker

        #Sets checkers coordinates to new area
        correspond_checker.set_coord(self.end_coord)

        #Gets row
        r = self.end_coord[0]

        #If the row is 0 or 7 promote to a king
        if correspond_checker.moves_forward() and r == 0:
            correspond_checker.promote_king()

        if not correspond_checker.moves_forward() and r == 7:
            correspond_checker.promote_king()

        #Update display
        self.update_display()

    def do_capture(self):
        '''Play_Checkers.do_capture()
        captures checker and plays move'''

        #Finds correct checker
        for checker in self.checker_list:
            if checker.get_position() == self.start_coord:
                correspond_checker = checker
        #Gets coord in between
        in_between_coord = ((self.start_coord[0] + self.end_coord[0])//2, (self.start_coord[1] + self.end_coord[1])/2)

        #Removes the checker in between 
        for checker in self.checker_list:
            if checker.get_position() == in_between_coord:
                self.checker_list.remove(checker)
                break     

        #Puts the capturing checker on the other coordinate
        correspond_checker.set_coord(self.end_coord)
        
        check_coords = self.end_coord
        
        r = check_coords[0]

        #Promotes to king if needed
        if correspond_checker.moves_forward() and r == 0:
            correspond_checker.promote_king()

        if not correspond_checker.moves_forward() and r == 7:
            correspond_checker.promote_king()

        self.board[in_between_coord].bind('<Button-1>', self.get_click)

        self.update_display()

    def can_checker_jump(self, checker_square):
        '''Play_Checkers.can_checker_jump(checker_square) -> Boolean
        Can see if checker has any legal jumps'''

        #Gets position
        checker_square_coord = checker_square.get_position()

        #If king
        if checker_square.get_checker().is_king():


            for possible_row_inc in range(-2, 3, 4):
                for possible_column_inc in range(-2, 3, 4):

                    
                    possible_row = checker_square.get_row() + possible_row_inc

                    possible_column = checker_square.get_column() + possible_column_inc

                    
                    
                    if possible_row > 7 or possible_row < 0 or possible_column < 0 or possible_column > 7:
                        continue

                    if self.board[(possible_row, possible_column)].has_checker():
                        continue


                    possible_coord = (possible_row, possible_column)
                    
                    if self.is_turn_legal(checker_square_coord, possible_coord):
                        
                        return True 
            
            return False

        #If white and not king
        elif checker_square.get_checker().moves_forward():

            for possible_column_inc in range(-2, 3, 4):

                #Iterates to see if it can
                #perform a capture with any of the legal squares in front of it
                possible_row = checker_square.get_row() - 2

                possible_column = checker_square.get_column() + possible_column_inc


                
                if possible_row < 0 or possible_column < 0 or possible_column > 7:
                    continue

                if self.board[(possible_row, possible_column)].has_checker():
                        continue


                possible_coord = (possible_row, possible_column)
                    
                if self.is_turn_legal(checker_square_coord, possible_coord):
                    return True 

            return False

        
        #If red and not king
        elif not checker_square.get_checker().moves_forward():
            
            for possible_column_inc in range(-2, 3, 4):

                #Iterates to see if it can
                #perform a capture with any of the legal squares in front of it

                possible_row = checker_square.get_row() + 2

                possible_column = checker_square.get_column() + possible_column_inc


                
                if possible_row > 7 or possible_column < 0 or possible_column > 7:
                    continue

                if self.board[(possible_row, possible_column)].has_checker():
                        continue


                possible_coord = (possible_row, possible_column)
                    
                if self.is_turn_legal(checker_square_coord, possible_coord):
                    return True 

            return False

    def take_turn(self, color):
        '''Play_Checkers.take_turn(color) -> Boolean
        Plays a checker turn for a color
        returns whether there is a targeted square that can only move'''

        #If there is no specific checker that is the only one that can move
        if self.specific_checker == None:

            #Finds opposite color
            if color == 'white':
                opp_color = 'red'

            else:
                opp_color = 'white'

            #Disables all checker_squares with checkers that are the opposite color
            for checker in self.checker_list:
                checker_coord = checker.get_position()
                if checker.get_color() == opp_color:
                    
                    self.board[checker_coord].unbind('<Button-1>')
                else:
                    self.board[checker_coord].bind('<Button-1>', self.get_click)
        #If there is a specified checker
        else:

            #Disables all checkers except for specificed checker that is
            #the only one that can move
            for checker in self.checker_list:
                checker_coord = checker.get_position()
                if checker == self.specific_checker_square:
                    self.board[checker_coord].bind('<Button-1>', self.get_click)
                    
                elif checker != self.specific_checker_square:
                    self.board[checker_coord].unbind('<Button-1>')
                  
        #Enable checkers 
                    
        self.enable_checkers()

        #If there is no specific checkers square return False, otherwise
        #return True
        if self.specific_checker_square == None:

            return False
        else:
            return True
                        
    def play_checkers(self):
        '''Play_Checkers.play_checkers()
        Starts checkers turn'''
        
        self.start_turn()
        
    def start_turn(self):
        '''Play_Checkers.start_turn()
        Sets player turn and checker color and then enables the checkers'''
        
        # Determine current player's color
        if self.currentPlayer == 0:
            color = 'white'
        else:
            color = 'red'

        # Enable the current player's checkers for selection
        self.enable_checkers(color)

    def enable_checkers(self, color):
        '''Play_Checkers.enable_checkers(color)
        Enables all checker_squares that are the specific color'''
        
        # Enable all checkers of the current player and disable the opponent's checkers
        for checker_square in self.board.values():
            if checker_square.has_checker() and checker_square.get_checker().get_color() != color:
                
                checker_square.unbind('<Button-1>')
                
            else:
                checker_square.bind('<Button-1>', self.get_click)
                
    def check_turn_end(self):
        '''Play_Checkers.check_turn_end()
        Checks to see if a turn should be ended'''
        
        if self.specific_checker_square == None:
            
            self.end_turn()  # End the turn if no more jumps are possible
            return True
        
        #If a checker can jump again    
        elif self.can_checker_jump(self.specific_checker_square):

            #Unbind all checkers except specific checker
            for checker_square in self.board.values():
                if checker_square != self.specific_checker_square and checker_square.has_checker():
                    checker_square.unbind('<Button-1>')

            self.specific_checker_square = None
            
            return False

        #Otherwise
        else:

            # The player can continue to make jumps; wait for another click
            
            self.end_turn()
            return True

    def end_turn(self):
        '''Play_Checkers.end_turn()
        Ends checkers turn and makes it the next turn'''

        #Check for win
        if self.check_has_won():
            #End game
            self.end_game()
            return

        #Switch current player
        self.currentPlayer = 1 - self.currentPlayer

        #Reset game label text
        self.gameLabel['text'] = ''

        #Sets color
        if self.currentPlayer == 0:
            color = 'white'

        if self.currentPlayer == 1:

            color = 'red'

        #Initializes data 
        self.capture = False

        self.specific_checker = None

        #Updates label that shows which checker turn it is

        self.play_color_label.remove_checker()

        self.display_checker = Checker(color, (8, 2))
        
        self.play_color_label.place_checker(self.display_checker)

        self.update_display()

        self.click_num = 0

        self.start_coord = None

        self.end_coord = None

        #Play checkers again with new side having the turn
        
        self.play_checkers()

    def check_has_won(self):
        '''Play_Checkers.check_has_won()
        Checks if a player has won'''

        #Get opposite color

        if self.currentPlayer == 1:
            opp_color = 'white'

        elif self.currentPlayer == 0:

            opp_color = 'red'

        #If other player cannot play a move then player wins
        for checker in self.checker_list:
            if checker.get_color() == opp_color:

                coord = checker.get_position()

                if checker.moves_forward() and not checker.is_king():

                    for column in range(-1, 2, 2):
                        coord_check = (coord[0] - 1, coord[1] + column)
                        if self.is_turn_legal(coord, coord_check):
                            return False

                    for column in range(-2, 3, 4):
                        coord_check = (coord[0] - 2, coord[1] + column)
                        if self.is_turn_legal(coord, coord_check):
                            return False

                elif not checker.moves_forward() and not checker.is_king():

                    for column in range(-1, 2, 2):
                        coord_check = (coord[0] + 1, coord[1] + column)
                        if self.is_turn_legal(coord, coord_check):
                            return False

                    for column in range(-2, 3, 4):
                        coord_check = (coord[0] + 2, coord[1] + column)
                        if self.is_turn_legal(coord, coord_check):
                            return False

                elif checker.is_king():

                    for row in range(-2, 3, 4):
                        for column in range(-2, 3, 4):
                            coord_check = (coord[0] + row, coord[1] + column)
                            if self.is_turn_legal(coord, coord_check):
                                return False

                    for row in range(-1, 2, 2):
                        for column in range(-1, 2, 2):
                            coord_check = (coord[0] + row, coord[1] + column)
                            if self.is_turn_legal(coord, coord_check):
                                return False
                
        #If no legal move is possible then this means that
        #there were either 0 checkers of the opposite color or
        #or that the other play could not play anything, so end game
        return True

    def end_game(self):
        '''Play_Checkers.end_game()
        Ends game and alerts who won'''

        #Get color of winning player
        
        if self.currentPlayer == 0:
            color = 'White'

        if self.currentPlayer == 1:

            color = 'Red'

        #Update game label for winning player
        self.gameLabel['text'] = f'Game over! {color} wins!'

        #Disable board
        for checker_square in self.board.values():

            checker_square.unbind('<Button-1>')
            
def play_checkers():
    '''play_checker()
    Plays Checkers game'''
     
    root = Tk()
    root.title('Checkers')
    Ch = Play_Checkers(root)
    root.mainloop()

play_checkers()

