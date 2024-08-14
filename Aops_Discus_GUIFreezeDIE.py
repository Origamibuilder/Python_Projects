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

class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6, frozen = False):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        GUIDie.__init__(self, master, valueList, colorList)

        self.frozen = frozen


    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''

        return self.frozen
    
    def toggle_freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''

        if self.frozen:
            self.frozen = False
            self['bg'] = 'white'
        else:
            self.frozen = True
            self['bg'] = 'gray'

    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''

        if self.frozen:
            return
        else:
            GUIDie.roll(self)

class Discus_Player(Frame):
    
    def __init__(self, master, name):
    
        
        # set up Frame object
        Frame.__init__(self, master)
        self.grid()
        # label for player's name
        Label(self, text=name, font=('Arial', 16)).grid(columnspan=3, sticky=W)
        # set up score and high score labels
        self.scoreLabel = Label(self, text='Attempt #1 Score: 0', font=('Arial', 13))
        self.scoreLabel.grid(row=0, column=2, columnspan=2)
        self.highScoreLabel = Label(self, text='High Score: 0', font=('Arial', 13))
        self.highScoreLabel.grid(row=0, column=5, columnspan=3, sticky=E)
        # initialize game data
        self.frozen = 0
        self.score = 0
        self.highscore = 0
        self.attempt = 1
        self.freeze = True
        self.first_turn = True
        # set up initial dice
        self.dice = []
        self.freezers = []
        for n in range(5):
            self.dice.append(GUIFreezeableDie(self, [1, 2, 3, 4, 5, 6], ['red'] + ['black'] + ['red'] + ['black'] + ['red'] + ['black']))
            self.dice[n].grid(row=1, column=n)
            self.freezers.append(Button(self, text='Freeze', state = DISABLED, command = self.dice[n].toggle_freeze))
            self.freezers[n].grid(row=2, column = n)

        self.rollButton = Button(self, text='Roll', command=self.roll)
        self.rollButton.grid(row=1, column = 5, columnspan=3)
        
        self.stopButton = Button(self, text='Stop', state=DISABLED, command=self.stop)
        self.stopButton.grid(row=2, column = 5, columnspan=3)

        self.gameLabel = Label(self, text='Click Roll Button To Start', font=('Arial', 15))
        self.gameLabel.grid(row=3, column = 0, columnspan=5)
        
        
    def roll(self):
        '''Shotput_Player_Frame.roll()
        handler method for the roll button click'''

        

        current_frozen = 0
        for dice in self.dice:
            if dice.is_frozen():
                current_frozen += 1

        if current_frozen - self.frozen > 0 or self.first_turn:
            self.freeze = True
        elif current_frozen - self.frozen == 0 and not self.first_turn:
            self.freeze = False
        

        self.first_turn = False
        

        self.frozen = current_frozen

        
        # roll dice
        if not self.freeze:
            self.gameLabel['text'] =  'You must freeze at least one dice to reroll.'
            self.gameLabel['font'] = ('Arial', 14)
            return

        self.first_turn = False

        
        
        for dice in self.dice:
            dice.roll()
                

        self.score = 0 

        num = 0

        even_active = 0

        odd = 0

        
        
        for button in self.freezers:
            if self.dice[num].get_top() % 2 == 0:
                self.score += self.dice[num].get_top()
            if self.dice[num].get_top() % 2 == 0 and not self.dice[num].is_frozen():
                self.freezers[num]['state'] = ACTIVE
                even_active += 1
            if self.dice[num].get_top() % 2 == 1:
                odd += 1
            if self.dice[num].is_frozen():
                self.freezers[num]['state'] = DISABLED
                
            num += 1

        self.gameLabel['text'] = 'Click Stop button to keep.'

        if odd > 0 and even_active == 0:
            self.scoreLabel['text'] = 'FOULED ATTEMPT'
            for button in self.freezers:
                button['state'] = DISABLED
            self.score = 0
            self.rollButton['state'] = DISABLED
            self.stopButton['state'] = ACTIVE
            self.stopButton['text'] = 'FOUL'
            self.scoreLabel['text'] = 'FOULED ATTEMPT'
            self.gameLabel['text'] = 'Click FOUL button to continue.'
            return
        
            
                

        #If first turn has passed, enable stop button
        if self.stopButton['state'] == DISABLED:
            self.stopButton['state'] = ACTIVE
            
        
        #Add dice roll to score 
        self.scoreLabel['text'] = 'Attempt #{} Score: {}'.format(self.attempt, self.score)

        self.freeze = False

        
    
            
    def stop(self):
        '''Shotput_Player_Frame.stop()
        handler method for the stop button click'''                     

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
            for button in self.freezers:
                button['state'] = DISABLED

            if self.highscore == 0:
                for i in range(25):
                    print("\nWhat??? \n:'(\nYour final high score was 0???")
            else:
                print('\nYOUR FINAL HIGH SCORE WAS {}!'.format(self.highscore))
            return
        
        #Activate roll button again in case of foul and reset position
        self.rollButton['state'] = ACTIVE


        self.stopButton['state'] = DISABLED

        self.dice = []
        self.freezers = []
        for n in range(5):
            self.dice.append(GUIFreezeableDie(self, [1, 2, 3, 4, 5, 6], ['red'] + ['black'] + ['red'] + ['black'] + ['red'] + ['black']))
            self.dice[n].grid(row=1, column=n)
            self.freezers.append(Button(self, text='Freeze', state = DISABLED, command = self.dice[n].toggle_freeze))
            self.freezers[n].grid(row=2, column = n)
            
        self.gameLabel['text'] = 'Click Roll Button To Start'

        self.first_turn = True

#play the game      
name = input("Enter your name: ")
root = Tk()
root.title('Discus')
game = Discus_Player(root, name)
game.mainloop()
