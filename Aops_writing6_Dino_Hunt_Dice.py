# Python Class 3962
# Lesson 6 Problem 5
# Author: origamibuilder (521817)

import random

### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
    '''implements one die for Dino Hunt'''

    def __init__(self, color):
        '''DinoDie(color)
        creates a new Dino game die object
        that has 6 sides'''

        self.color = color

        if self.color == 'green':
            Die.__init__(self, ['dino', 'dino', 'dino', 'leaf', 'leaf', 'foot'])

        elif self.color == 'yellow':
            Die.__init__(self, ['dino', 'dino', 'leaf', 'leaf', 'foot', 'foot'])
            

        elif self.color == 'red':
            Die.__init__(self, ['dino', 'leaf', 'leaf', 'foot', 'foot', 'foot'])
            
        

    def __str__(self):
        '''str(DinoDie) -> str
        string representation of Dino Die'''
        
        return f'A {self.get_color()} Dino die with a {self.get_top()} on top.'
            
    def get_color(self):
        '''DinoDie.get_color() -> str
        returns dino dices color'''

        return self.color
        

        
         

class DinoPlayer:
    '''implements a player of Dino Hunt'''

    def __init__(self, name):
        '''DinoPlayer(name)
        creates a new Dino Player object
        Player has 6 Green Dino Die, 4 Yellow Dino Die, and 3 Red Dino Die
        Players name is name'''

        self.name = name

        self.points = 0

        self.inv = []

        for num in range(6):
            self.inv.append(DinoDie('green'))

        for num in range(4):
            self.inv.append(DinoDie('yellow'))

        for num in range(3):
            self.inv.append(DinoDie('red'))

        self.numGreen = 6

        self.numYellow = 4

        self.numRed = 3

    def __str__(self):
        '''str(DinoPlayer) -> str
        string of how many die the player has left'''

        return f'You have {len(self.inv)} dice left. '

    def get_name(self):
        '''DinoPlayer.get_name() -> str
        returns players name'''

        return self.name

    def get_inv(self):
        '''DinoPlayer.get_inv() -> str
        returns string of the number of green, yellow,
        and red Dino Die the player has'''

        return f'{self.numGreen} green, {self.numYellow} yellow, {self.numRed} red'

    def get_points(self):
        '''DinoPlayer.get_points() -> str
        returns string of how many points player has'''

        return str(self.points)

    def add_points(self, points):
        '''DinoPlayer.add_points(points)
        Adds a set number of points to player'''

        self.points += points


    
            

def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''

    playerList = []

    for num in range(numPlayers):

        name = input(f'Player {num + 1}, what is your name? ')

        playerList.append(DinoPlayer(name))

    #Gets player names and initializes players

    for rounds in range(numRounds): #For every round
        print(f'\nROUND {rounds + 1}!\n')

        for player in playerList:
                print(f'{player.get_name()} has {player.get_points()} points')


        for player in playerList: #For every player

            
            print('\n')
            print(f"{player.get_name()}, it's your turn! ")
            print('\n')

            stomp_status = False #Player has not been stomped

            feet = 0 #Number of feet player has collected this turn

            dinos = 0 #Number of dinos player has collected this turn

            while True: #Until player ends turn or gets stomped
                
                if len(player.inv) == 0:
                    print(f"{player.get_name()}, you have 0 dice left in your inventory, so your score is final! ")
                    break #If player has 0 dice left, end their turn


                print(player)
                print(player.get_inv())
                turn = input('Press enter to select dice and roll. ')
                rolled_dice = []
                
                if len(player.inv) > 2: #If 3 or more dice remain
                    for dice in range(3): #Extracts dice randomly using random.randrange() method
                        die = player.inv.pop(random.randrange(len(player.inv)))
                        die.roll() #Use list.pop() method and roll this dice 
                        print(die)
                        rolled_dice.append(die)

                        
                else: #If 1 or 2 dice remain
                    print('You only have {len(player.inv)} dice left. ') 
                    for dice in range(len(player.inv)):
                        die = player.inv[random.randrange(len(player.inv))].pop()
                        die.roll()
                        print(die)
                        rolled_dice.append(die)
                        

                for die in rolled_dice:
                    if die.get_top() == 'leaf':
                            player.inv.append(die) #If top is leaf, put it back in inventory

                    elif die.get_top() == 'dino':
                        dinos += 1 #Increment dinos
                        if die.color == 'green':
                            player.numGreen -= 1 

                        elif die.color == 'yellow':
                            player.numYellow -= 1

                        else:
                            player.numRed -= 1

                        #If dice is permanently going to be removed, remove one of its color from the player

                    else:
                        feet += 1 #Increment feet
                        
                        if die.color == 'green':
                            player.numGreen -= 1

                        elif die.color == 'yellow':
                            player.numYellow -= 1
                        else:
                            player.numRed -= 1
                        
                        
                                

                if feet >= 3: #If player has 3 or more feet, stomp it
                    print('Too bad -- You have been stomped! ')
                    stomp_status = True #Stomp status true 
                    break

                print(f'This turn so far: {str(dinos)} dinos and {str(feet)} feet. ')

                reroll = '' 

                while reroll not in ['y', 'n']:
                    reroll = input('\nDo you want to roll again? (y/n) ')

                    #If user wants to roll again, let them

                if reroll == 'n':
                    break 

                
                

            if not stomp_status: #If stomp status is not true, add the players dino points
                player.add_points(dinos)

    winner_list = []

    best_score = 0

    for player in playerList:
        if int(player.get_points()) > best_score:
            best_score = int(player.get_points()) #Finds highest score

    for player in playerList:
        if int(player.get_points()) == best_score:
            winner_list.append(player)#Whoevers score matches the best score is added to winner list
    print('\n\n')
    if len(winner_list) == 0: #If everyone has 0 points, tell them 
        print('No one got a single point so no one wins. Too bad. ')
    if len(winner_list) == 1: #If one person wins, tell them
        print('We have a winner! ')
        print(f'{winner_list[0].get_name()} has {winner_list[0].get_points()} points.')
    else: #If multiple people have best score, alert them that there is a tie and ask them 
        tie_string = f'\nWe have a tie for first between the following {len(winner_list)} players:'
        for player in winner_list:
            tie_string += f'\n{player.get_name()}'

        print(tie_string)

        replay = input('Play again to decide who the greatest Dino Hunt Dice player is? (y/n) ')
        if replay == 'y':
            print('\n\n\n')
            play_dino_hunt(numPlayers, numRounds)
            

play_dino_hunt(2, 1)

'''
Technical Score: 7 / 7
Style Score: 0.6 / 1
Comments:
You've submitted a nice solution for this problem! You have correctly implemented the functionality needed to play the game, you keep track of the total points and the current stomps correctly as well. Let's see what can be improved.

Good job calling the parent class $\verb#__init__#$ method in the constructor of $\verb#DinoDie#$ the way you did! This was the key practice for inheritance in this week's assignment.

You seem to have chosen to implement everything for this game in one main gameplay function. While acceptable, it's not necessarily the most optimal solution. The first reason being it's become quite big. The second being that the logic behind a player's turn is more suited to reside in a method inside the Player class, since that class take the responsibility of handling the player's actions and state. Try to refactor your code so that you have an appropriate $\verb#take_turn#$ method in your Player class as extra practice!

Lines 206 to 211 and from 214 to 220 are quite similar and can be extracted in a separate function with an appropriate argument passed to it. Moreover, you can eliminate the need for that and the if clause by modifying the argument for the $\verb#range#$ function:

for die in range(min(3, len(len(player.get_inv())))):

This will automatically roll 3 dice if there are at least 3 dice in the $\verb#dice#$ variable, and all the dice otherwise.

On line 208, you're accessing the $\verb#inv#$ attribute of a Player object directly from outside that class. This goes against the OOP principles, because you're exposing the implementation of the class to the outside world. If you want to use a property of a class from outside that class, you'll have to implement setters and getters and use them instead.

Good job handling the case when there could be a tie between the winners! This improves your game's overall user experience.

In terms of style, good job using meaningful variable names! Kudos for adding comments in key places of your code, as well as docstrings for your methods! This boosts your overall style and readability.

Nice work describing your approach in the text box! However, don't forget to include information about testing, too, since that's the only way we can be sure our code works as expected. Here, it would be a good idea to make sure the gameplay mechanics surrounding the dino and feet dice are all in place. It would be even better if you paste the output of the console for a small game or even attach screenshots of it. Make sure to keep this in mind for your future submissions.

Stay motivated and keep practicing!

Your Response:
DinoDie:

__init__:
Uses inheritance of the Die class with cases leading to different die being created. Since the die class already accounts for lists of special die sides, the program just imports the Die __init__ and uses a corresponding color to match up with a different, preset list which is then put in.

__str__:
The same string as Die, but it returns that the die is also a Dino Die and it returns the Die's color.

get_color():
Just returns the Dino Die's color.



DinoPlayer:

__init__:
Initializes a Dino Player and uses a for loop to add 6 green die, 4 yellow die, and 3 die to self.inv (inventory). It also defines the number of green, yellow, and red the player has.

__str__:

Outputs the number of dice the player has left in their inventory.

get_name():

Returns player's name

get_inv():

Outputs the number of green, yellow, and red die the player has.

get_points():

Outputs the number of points the player has.

add_points(points):

Adds a set number of points to the player



play_dino_hunt:

After initializing and creating every player, uses for loops (since the number of rounds are preset) to run through each round and to run through each player in each round. Uses a while loop that breaks once the player has no dice left, they have been stomped, or until they end their turn. At the end, finds the player with the best score, and alerts who it was (unless it was a tie or if no one got any points).
'''
                

                
                            
                    
                

                
        

        
