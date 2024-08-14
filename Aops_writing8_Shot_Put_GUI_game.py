# Python Class 3962
# Lesson 8 Problem 2
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

class Shotput_Player_Frame(Frame):
    '''frame for a game of Shotput'''

    def __init__(self, master, name):
        '''Shotput_Player_Frame(master,name) -> Shotput_Player_Frame
        creates a new Shotput frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self, master)
        self.grid()
        # label for player's name
        Label(self, text=name, font=('Arial', 16)).grid(columnspan=3, sticky=W)
        # set up score and high score labels
        self.scoreLabel = Label(self, text='Attempt #1 Score: 0', font=('Arial', 13))
        self.scoreLabel.grid(row=0, column=3, columnspan=2)
        self.highScoreLabel = Label(self, text='High Score: 0', font=('Arial', 13))
        self.highScoreLabel.grid(row=0, column=5, columnspan=3, sticky=E)
        # initialize game data
        self.turn = 0
        self.score = 0
        self.highscore = 0
        self.attempt = 1
        # set up initial dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, 6], ['red'] + ['black'] * 5))
            self.dice[n].grid(row=1, column=n)
        # set up buttons
        self.rollButton = Button(self, text='Roll', command=self.roll)
        self.rollButton.grid(row=2, columnspan=1)
        self.stopButton = Button(self, text='Stop', state=DISABLED, command=self.stop)
        self.stopButton.grid(row=3, columnspan=1)

        

    def roll(self):
        '''Shotput_Player_Frame.roll()
        handler method for the roll button click'''
        # roll dice
        self.dice[self.turn].roll()

        #If first turn has passed, enable stop button
        if self.stopButton['state'] == DISABLED:
            self.stopButton['state'] = ACTIVE
            
        #If foul, set score to 0 and end attempt
        if self.dice[self.turn].get_top() == 1:           
            self.score = 0
            self.rollButton['state'] = DISABLED
            self.stopButton['text'] = 'FOUL'
            self.scoreLabel['text'] = 'FOULED ATTEMPT'
            return
        
        #Add dice roll to score 
        self.score += self.dice[self.turn].get_top()

        self.scoreLabel['text'] = 'Attempt #{} Score: {}'.format(self.attempt, self.score)

        #Increment turn
        self.turn += 1

        #If no turns are left, stop turn and total
        if self.turn == 8:
            self.stop()
        else:
            #If turns are left, increment button columns
            self.rollButton.grid(row = 2, column = self.turn)
            self.stopButton.grid(row = 3, column = self.turn)

            
    def stop(self):
        '''Shotput_Player_Frame.stop()
        handler method for the stop button click'''                     

        #Reset turn    
        self.turn = 0

        #If score is greater than highscore, make new highscore score 
        if self.score > self.highscore:
            self.highscore = self.score
            self.highScoreLabel['text'] = 'Highscore: {}'.format(self.highscore)
        #Reset score      
        self.score = 0

        
        self.attempt += 1 #Increment attempt number and reset score board
        if self.attempt != 4:
            self.scoreLabel['text'] = 'Attempt #{} Score: 0'.format(self.attempt)

        self.stopButton['text'] = 'Stop'

        
        #If 3 attempts are done, delete buttons 
        # and announce that the game is over   
        if self.attempt == 4:
            self.scoreLabel['text'] = 'Game Over!'
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()

            if self.highscore == 0:
                for num in range(25):
                    print("\nWhat??? \n:'(\nYour final high score was 0???")
            else:
                print('\nYOUR FINAL HIGH SCORE WAS {}!'.format(self.highscore))
            return
        
        #Activate roll button again in case of foul and reset position
        self.rollButton['state'] = ACTIVE

        self.rollButton.grid(row=2, column = 0, columnspan=1)

        #Deactivate stop button for first turn and reset postion
        self.stopButton['state'] = DISABLED

        self.stopButton.grid(row=3, column = 0, columnspan=1)

        # set up dice again for next turn
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, 6], ['red'] + ['black'] * 5))
            self.dice[n].grid(row=1, column=n)
        


#play the game      
name = input("Enter your name: ")
root = Tk()
root.title('Shotput')
game = Shotput_Player_Frame(root, name)
game.mainloop()


