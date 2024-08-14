#Python Class 3962
# Lesson 10 Problem 1
# Author: origamibuilder (521817)

#imports
from tkinter import *
from tkinter import messagebox
import random



class mine_square(Label):
    '''Creates a mine square'''
    

    def __init__(self, master, square_type, colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray']):
        '''mine_square(master, square_type, color_map) -> Mine Square
        creates a new blank Mine Square that is either a bomb or normal
        Alterable colormap already set'''

        #Creates the Square
        Label.__init__(self, master, height=1, width = 2, text='', \
                       bg='white', font=('Arial', 24), relief = RAISED)

        #Nothing on the mine square
        self.status = 'blank'
        
        # set up listeners
        self.bind('<Button-1>', self.update)
        self.bind('<Button-3>', self.update)

        #Has the area around the mine square been exposed 
        self.exposed = False

        self.square_type = square_type

        self.colormap = colormap
        
        #Not known how many surrounding bombs there are yet
        self.surround_bombs = None

        #Square is not visible yet
        self.is_visible = False

    
    def update(self, event):
        '''mine_square.update(event)
        Updates cell status based on user click and then updates display'''
        

        if self.is_square_visible():
            return
        
        # only act if the cell is not visible yet

        
        #If left click
        if event.num == 1:
            if not self.status == 'aster':
                self.status = 'num' #Expose square and set status to a number
                    
                    
                if self.is_bomb(): #If it is a bomb, explode it and update
                        
                    self.status = 'detonated'
                        
                    self.update_display()

                    return
         
                elif self.is_blank():

                    #If it has no surrounding blanks, update display 
                    self.update_display()
                    #Activate master update_blanks() method
                    self.master.update_blanks()
                    return   

        #If right click    
        elif event.num == 3:
            #If button is asterick make it blank, and vice versa
            if self.status == 'aster':
                self.status = 'blank'
            elif self.status == 'blank':
                self.status = 'aster'

        #Update display

        self.update_display()

    def update_display(self):

        #If already visible, return
        if self.is_square_visible():
            return
        
        #If asterick, make text an asterick
        if self.status == 'aster':
            self['font'] = ('Arial', 24)
            self['text'] = '*'

        
        #If status is num
        elif self.status == 'num':

            #Make text blank
            self['text'] = ''

            #If there are surrounding bombs
            if not self.is_blank():

                #Change the text of square to the number of surrounding bombs and use colormap to update color
                color = self.colormap[self.get_surrounding_bombs()]
                self['fg'] = color
                self['text'] = str(self.get_surrounding_bombs())

            #Make background lightgray and relief Sunken
            self['bg'] = 'lightgray'
            self['relief'] = SUNKEN

            #Is now visible
            self.is_visible = True

            
            #Update master's label
            self.master.update_normal_label()
            
        #If bomb is detonated
        elif self.status == 'detonated':
            #Make text asterick, make asterick bg darkred, and make relief Sunken
            self['text'] = '*'
            self['bg'] = 'darkred'
            self['relief'] = SUNKEN
            self.is_visible = True
            
            #If it has not already lost, make it lose
            if not self.master.has_lost():
                self.master.lose()

        #If status is blank
        else:
            #Change font and change text to blank
            self['font'] = ('Arial', 24)
            self['text'] = ''

        
    def set_surround_bombs(self, num):
        '''mine_square.set_surround_bombs(num)
        Input the number of bombs that surround the square'''

        self.surround_bombs = num

    def get_surrounding_bombs(self):
        '''mine_square.get_surrounding_bombs() - int
        returns the number of bombs surroundnig the square'''
        return self.surround_bombs


    def get_type(self):
        '''mine_square.get_type() -> str
        returns status of the square'''
        return self.status

    def is_bomb(self):
        '''mine_square.is_bomb() -> boolean
        returns if the square is a bomb or not'''

        return self.square_type == 'bomb'

    def is_blank(self):
        '''mine_square.is_bomb() -> boolean
        returns if the square has no bombs around it'''

        return self.get_surrounding_bombs() == 0

    def is_area_already_exposed(self):
        '''mine_square.is_area_already_exposed() -> boolean
        returns whether the area surrounding square has already been exposed
        Meant for squares that are blank*'''

        return self.exposed

    def is_square_visible(self):
        '''mine.is_square_visible -> boolean
        returns if the square is visible and has already been clicked'''

        return self.is_visible

    def set_status(self, status):
        '''mine_square.set_status(status)
        sets the status of the mine square'''

        self.status = status

    def set_exposed(self):
        '''mine_square.set_exposed()
        toggles the mine square to its surrounding area being exposed'''

        self.exposed = True



class MineFrame(Frame):

    def __init__(self, master, width, height, numBombs):

        
        #Frame inheriance
        Frame.__init__(self, master, bg = 'black')

        #Grid
        self.grid()

        #Creates list that stores random values that will be where the bombs are
        self.randlist = []

        #For every bomb that there is supposed to be
        for i in range(numBombs):
            while True: #Until a new place for a bomb is created
                #Update list 
                num = random.randint(0, (width * height) - 1)
                if num not in self.randlist:
                    self.randlist.append(num)
                    break

        
        self.height = height

        self.width = width
        
        num = 0

        #Dictionary that stores all of the mines with the index beig the coord
        self.mineDict = {}
        for row in range(height):
            for column in range(width):
                coord = (row, column)
                if num in self.randlist: #If it is bomb from random list
                    self.mineDict[coord] = mine_square(self, 'bomb')
                    # cells go in even-numbered rows/columns of the grid
                else: #If it is not a bomb from random list
                    self.mineDict[coord] = mine_square(self, 'normal')

                #Set mines place
                self.mineDict[coord].grid(row = 2 * row, column = 2 * column)
                
                num += 1

        #For every mine, if it is not a bomb, update how many bombs are surrounding the mine
        for mine in self.mineDict:
            bombs = 0
            
            row = mine[0]
            column = mine[1]

            coord = (row, column)

            #If bomb, pass mine
            if self.mineDict[coord].is_bomb():
                continue

            #For every mine one next to current mine
            for row_increment in range(-1, 2):
                for column_increment in range(-1, 2):

                    if row_increment == 0 and column_increment == 0:
                        continue
                    #If current_mine is actual mine, skip
                    
                    #Current_bomb row and column
                    current_row = row + row_increment

                    current_column = column + column_increment

                    #Makes sure that column or row are not going out of index
                    if current_column < 0 or current_column > width - 1 or current_row < 0 or current_row > height - 1:
                        continue

                    #Coordinate that checks
                    coord_check = (current_row, current_column)

                    #If mine is bomb, increment number of bombs
                    if self.mineDict[coord_check].is_bomb():
                        bombs += 1
                        
            #Set mine as having this many bombs
            self.mineDict[coord].set_surround_bombs(bombs)


        #Number of normal squares 
        self.num_exposed_normal_squares = (width * height) - numBombs

        #Label that displays the number of normal squares
        self.numNormalLabel = Label(self, text = str(self.num_exposed_normal_squares), font = ('Arial', 24))

        #Put label at bottom of game
        self.numNormalLabel.grid(row = height * 2, column = 0, columnspan = width * 2 - 1)

        #Player has not lost yet
        self.lose_status = False


    def update_normal_label(self):
        '''MineFrame.update_normal_label()
        update label and subtract 1 from the number of nonexposed squares'''
        self.num_exposed_normal_squares -= 1
        self.numNormalLabel['text'] = str(self.num_exposed_normal_squares)

        #If no squares are left, player wins
        if self.num_exposed_normal_squares == 0:
            self.win()

    def update_blanks(self):
        '''MineFrame.update_blanks()
        automatically updates surrounding mines of all new blank squares
        after each turn'''

        #Preset num
        num = 1

        #Until number of new blank squares is 0 
        while num > 0:
            num = 0

            #For every mine in mineDict
            for row in range(self.height):
                for column in range(self.width):

                    #Current mine coord
                    coord = (row, column)

                    mine = self.mineDict[coord]
                   

                    #If mine has no surrounding bombs and if the surrounding area has not already been exposed
                    #and if the mine is now visible
                    if mine.is_blank() and not mine.is_area_already_exposed() and mine.is_square_visible():
                        #Set mine as now having its surrounding area already exposed
                        mine.set_exposed()

                        #Increment num of new blank squares
                        num += 1

                        #Update all surrounding squares of blanks square 
                        for row_increment in range(-1, 2):
                            for column_increment in range(-1, 2):
                                if row_increment == 0 and column_increment == 0:
                                    continue
                                current_row = row + row_increment

                                current_column = column + column_increment

                                if current_column < 0 or current_column > self.width - 1 or current_row < 0 or current_row > self.height - 1:
                                    continue

                                coord_check = (current_row, current_column)

                                #Surrounding mine
                                neighbor_mine = self.mineDict[coord_check]

                                #If mine is not already visible, make it visible
                                if not neighbor_mine.is_square_visible():
                                    self.mineDict[coord_check].set_status('num')
                                    self.mineDict[coord_check].update_display()              


    def win(self):
        '''MineFrame.win()
        shows message box that shows user has won and disables game
        marks all bombs with asterisks'''
        messagebox.showinfo('Minesweeper','Congratulations -- you won!',parent=self)
        for row in range(self.height):
                for column in range(self.width):
                    
                    coord = (row, column)

                    mine = self.mineDict[coord]

                    if mine.is_bomb():
                        mine['text'] = '*'
                        
                    
                    mine.is_visible = True

    def lose(self):
        '''MineFrame.lose()
        shows message box that shows user has lost and disables game
        Shows all mines that have not been found as detonated'''

        
        self.lose_status = True
        messagebox.showerror('Minesweeper','KABOOM! You lose.',parent=self)
        for row in range(self.height):
                for column in range(self.width):
                    
                    coord = (row, column)
                    mine = self.mineDict[coord]

                    #Make every bomb visible if not already 
                    if mine.is_bomb():
                        if not mine.is_square_visible():
                            if not mine.status == 'aster':
                                mine.set_status('detonated')
                                mine.update_display()

                    if mine.status == 'aster' and not mine.is_bomb():
                        mine['text'] = ''
        
                    mine.is_visible = True


    def has_lost(self):

        '''MineFrame.has_lost() -> boolean
        Display if player has lost'''

        return self.lose_status
            


            
def play_minesweeper(width, height, numBombs):
    '''play_minesweeper(width, height, numBombs
    player minesweeper with set height and width and number of bombs'''


    #Checks for any errors in the user's inputted dimensions
    
    if isinstance(width, str) or isinstance(height, str) or isinstance(numBombs, str):
        print('Please input an integer number for width, height, and/or bomb.')
        return
    if numBombs < 0:
        print('You cannot have a negative number of bombs. ')
        return

    if numBombs > width * height:
        print('You cannot have a greater number of bombs than squares. ')
        return

    if width > 35 or height > 18:
        print('Error. Size too large. Please make sure that your height is 18 or under and that your width is 35 or under.')
        return

    #Plays minesweeper
    root = Tk()
    root.title('Minesweeper')
    game = MineFrame(root, width, height, numBombs)
    root.mainloop()
            

play_minesweeper(20, 15, 6)  

    
        
#
