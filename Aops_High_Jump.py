# Python Class 3962
# Lesson 8 Problem 3 Part (a)
# Author: origamibuilder (521817)

from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self, master, width=60, height=60, bg='white', bd=5, relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top - 1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1, 7)
        self.draw()

    def draw(self):
        """GUIDie.draw()
        draws the pips on the die"""
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [
            [(1, 1)],
            [(0, 0), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 0), (0, 2), (2, 0), (2, 2)],
            [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
            [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
        ]
        for location in pipList[self.top - 1]:
            self.draw_pip(location, self.colorList[self.top - 1])

    def draw_pip(self, location, color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx, centery) = (15 + 20 * location[1], 15 + 20 * location[0])  # center
        self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)


class High_Jump_Player(Frame):
    
    def __init__(self, master, name):
    
        
        # set up Frame object
        Frame.__init__(self, master)
        self.grid()
        # label for player's name
        Label(self, text=name, font=('Arial', 14)).grid(columnspan=3, sticky=W)
        # set up score and high score labels
        self.jumpLabel = Label(self, text='Attempt #1 Current Height: 10', font=('Arial', 13))
        self.jumpLabel.grid(row=0, column=1, columnspan=3)
        self.bestScoreLabel = Label(self, text='Best Height: 0', font=('Arial', 13))
        self.bestScoreLabel.grid(row=0, column=5, columnspan=4, sticky=E)
        # initialize game data
        self.height = 10
        self.score = 0
        self.attempt = 1
        self.end_game = False
        # set up initial dice
        self.dice = []
        for n in range(5):
            self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, 6], ['black'] * 6))
            self.dice[n].grid(row=1, column=n)

        self.rollButton = Button(self, text='Roll', command=self.roll)
        self.rollButton.grid(row=1, column = 5, columnspan=3)
        
        self.stopButton = Button(self, text='Skip Height', state=ACTIVE, command=self.end_turn)
        self.stopButton.grid(row=2, column = 5, columnspan=3)

        self.gameLabel = Label(self, text='Click Roll Button To Start or Skip Height', font=('Arial', 13))
        self.gameLabel.grid(row=3, column = 0, columnspan=5)
        
        
    def roll(self):
        
        jump = 0 

        for dice in self.dice:
            dice.roll()
            jump += dice.get_top()

        if jump < self.height:
            self.attempt += 1
            self.gameLabel['text'] = f'MISS! HEIGHT WAS {jump}. TRY AGAIN!'
            self.stopButton['state'] = DISABLED
        else:
            self.gameLabel['text'] = f'YOU MADE IT WITH A HEIGHT OF {jump}!'
            self.score = self.height
            self.bestScoreLabel['text'] = 'Best Height: {}'.format(self.score)
            self.rollButton['state'] = DISABLED
            self.stopButton['state'] = ACTIVE
            self.stopButton['text'] = 'END HEIGHT'
            return
            
            


        if self.attempt == 4:
            self.rollButton['state'] = DISABLED
            self.stopButton['state'] = ACTIVE
            self.stopButton['text'] = 'FAIL'
            self.bestScoreLabel['text'] = 'FAILED ATTEMPT'
            self.gameLabel['text'] = 'MISS! Click FAIL button to END GAME!'
            self.end_game = True
            return
        
            
        if self.stopButton['state'] == ACTIVE:
            self.stopButton['state'] = DISABLED
            
        #Add dice roll to score 
        self.bestScoreLabel['text'] = 'BEST SCORE: {}'.format(self.attempt, self.score)

        
    def end_turn(self):

        if self.end_game:
            self.jumpLabel['text'] = 'Game Over!'
            self.bestScoreLabel['text'] = f'Best Height: {self.score}'
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.gameLabel.grid_remove()

            if self.score == 0:
                for i in range(25):
                    print("\nWhat??? \n:'(\nYour final high score was 0???")
            else:
                print('\nYOUR FINAL HIGH SCORE WAS {}!'.format(self.score))
            return

        self.attempt = 1

        self.stopButton['state'] = ACTIVE

        self.stopButton['text'] = 'Skip'

        self.gameLabel['text'] = 'Click Roll Button to Start or Skip Height'


        self.rollButton['state'] = ACTIVE


        self.dice = []
        for n in range(5):
            self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, 6], ['black'] * 6))
            self.dice[n].grid(row=1, column=n)
            

        self.height += 2

        self.jumpLabel['text'] =  'Attempt #1 Current Height: {}'.format(self.height)

#play the game      
name = input("Enter your name: ")
root = Tk()
root.title('High Jump')
game = High_Jump_Player(root, name)
game.mainloop()
