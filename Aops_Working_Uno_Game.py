# Python Class 3962
# Lesson 5 Problem 1
# Author: origamibuilder (521817)
import random

import time

class UnoCard:
    '''represents an Uno card
    attributes:
      rank: int from 0 to 9 or action cards that contain colors
      color: string'''
    
    
    def __init__(self, rank, color = '', status = 'enabled'):
        '''UnoCard(rank, color, status) -> UnoCard
        creates an Uno card with the given rank (or special value) and color (and status for special cards)'''

        self.rank = rank
        self.color = color
        self.status = status

    def __str__(self):
        '''str(Unocard) -> str'''
        if self.rank == 'wild':
            if self.color != '':
                return str(f'Wild Card that is {self.color}.')
            return str(f'Wild Card')

        if self.rank == 'wildDrawFour':
            if self.color != '':
                return str(f'Wild Draw Four that is {self.color}')
            return str(f'Wild Draw Four')

        
        return(str(self.color) + ' ' + str(self.rank))

    def is_match(self, other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        if self.rank == 'wild':
            return True #Automatically a match if the card is a wild card
        return (self.color == other.color) or (self.rank == other.rank)


class UnoDeck:
    '''represents a deck of Uno cards
    attribute:
      deck: list of UnoCards'''

    def __init__(self):
        '''UnoDeck() -> UnoDeck
        creates a new full Uno deck'''
        self.deck = []
        for color in ['red', 'blue', 'green', 'yellow']:
            self.deck.append(UnoCard('wild')) #Adds 4 wild cards
            self.deck.append(UnoCard('wildDrawFour')) #Adds four draw four wild cards
            self.deck.append(UnoCard(0, color))  # one 0 of each color
            for i in range(2):           
                for n in range(1, 10):  # two of each of 1-9 of each color
                    self.deck.append(UnoCard(n, color))
                for action in ['reverse', 'skip', 'drawTwo']: #Two of each special card of each color
                    self.deck.append(UnoCard(action, color))
            
                
                    
        random.shuffle(self.deck)  # shuffle the deck

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'An Uno deck with '+str(len(self.deck)) + ' cards remaining.'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self, pile):
        '''UnoDeck.reset_deck(pile) -> None
        resets the deck from the pile'''
        if len(self.deck) != 0:
            return
        self.deck = pile.reset_pile() # get cards from the pile
        random.shuffle(self.deck)  # shuffle the deck

class UnoPile:
    '''represents the discard pile in Uno
    attribute:
      pile: list of UnoCards'''

    def __init__(self, deck):
        '''UnoPile(deck) -> UnoPile
        creates a new pile by drawing a card from the deck'''
        
        card = deck.deal_card()
        card.status = 'disabled'
        self.pile = [card]  # all the cards in the pile

    def __str__(self):
        '''str(UnoPile) -> str'''
        return 'The pile has a ' + str(self.pile[-1]) + ' on top.'

    def top_card(self):
        '''UnoPile.top_card() -> UnoCard
        returns the top card in the pile'''

        return self.pile[-1]

    def add_card(self, card):
        '''UnoPile.add_card(card) -> None
        adds the card to the top of the pile'''
        self.pile.append(card)

    def reset_pile(self):
        '''UnoPile.reset_pile() -> list
        removes all but the top card from the pile and
          returns the rest of the cards as a list of UnoCards'''
        for card in self.pile[:-1]:
            card.status = 'enabled'
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck

class UnoPlayer:
    '''represents a player of Uno
    attributes:
      name: a string with the player's name
      hand: a list of UnoCards'''

    def __init__(self, name, deck, cpu = False):
        '''UnoPlayer(name, deck, cpu) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]
        self.cpu = cpu

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        
        return str(self.name) + ' has ' + str(len(self.hand)) + ' cards.'

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def is_cpu(self):
        '''UnoPlayer.is_cpu() -> Boolean
        returns if player is a computer'''
        return self.cpu        

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self, deck):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self, card, pile):
        '''UnoPlayer.play_card(card, pile) -> None
        plays a card from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)

    def take_turn(self, deck, pile):
        '''UnoPlayer.take_turn(deck, pile) -> None
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile'''


        # get a list of cards that can be played
        topcard = pile.top_card()
        matches = [card for card in self.hand if card.is_match(topcard)]

        drawFourPlay = True 
        for card in self.hand:
            if card.color == topcard.color:
                drawFourPlay = False
                break

        if drawFourPlay == True:
            for card in self.hand:
                if card.rank == 'wildDrawFour':
                    matches.append(card)
        
        # print player info
        if self.is_cpu():
            print(f"It is {self.get_name()}'s turn. ")
            time.sleep(0.5)


            if len(matches) == 0:
                print(f"{self.get_name()} has no matches, so it has to draw a card. ")
                time.sleep(0.5)
                newcard = self.draw_card(deck)
                print(f"{self.get_name()} drew a {newcard}\n")

                time.sleep(0.5)

                if newcard.is_match(topcard): # can be played
                    print(f"\nThe computer can play the {newcard} and has played it.")
                    self.play_card(newcard,pile)
                else:   # still can't play
                    print("\nThe computer can still not play this card.")

                print('\n')

                time.sleep(0.5)
                
                return    
            
        
            



            color_values = {'red': 0, 'green': 0, 'blue': 0, 'yellow': 0}
            
            for card in self.hand:
                if card.color in color_values:
                    color_values[card.color] += 1


            total_color_count = sum(color_values.values())
            
            if total_color_count == 0:
                rand_card = random.choice(matches)
                self.play_card(rand_card, pile)
                print(f'{self.get_name()} has played a {rand_card}.')
                
                return

           

            color_match = []

            sorted_color_values = dict(sorted(color_values.items(), key=lambda item: item[1], reverse=True))
                
            for color in sorted_color_values:
                color_match.append(color)

        
            index = 0

            break_status = False

            
            while True:
                for match in matches:
                    if match.color == color_match[index]:
                        self.play_card(match, pile)
                        print(f'{self.get_name()} has chosen to play a {match}.')
                        return
                        
                
                index += 1
                if index > 3:
                    break

            rand_card = random.choice(matches)
            self.play_card(rand_card, pile)
            print(f'{self.get_name()} has played a {rand_card}.')

            return


            

                

            
        print(f"{self.name}, it's your turn.\n")
        print(str(pile) + '\n')
        print("Your hand: ")
        print(self.get_hand())
        

        
        
        if len(matches) > 0:  # can play
            for index in range(len(matches)):
                # print the playable cards with their number
                print(str(index + 1) + ": " + str(matches[index]))
            # get player's choice of which card to play
            choice = 0
            while choice < 1 or choice > len(matches):
                choicestr = input("\nWhich do you want to play? ")
                if choicestr.isdigit():
                    choice = int(choicestr)
            # play the chosen card from hand, add it to the pile
            self.play_card(matches[choice - 1], pile)
        else:  # can't play
            print("You can't play, so you have to draw.")
            input("Press enter to draw. ")
            # check if deck is empty -- if so, reset it                                                           
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = self.draw_card(deck)
            print("You drew: "+str(newcard))
            if newcard.is_match(topcard): # can be played
                print("Good -- you can play that!")
                self.play_card(newcard,pile)
            else:   # still can't play
                print("Sorry, you still can't play.")

        return
                      
def play_uno(numPlayers):
    '''play_uno(numPlayers) -> None
    plays a game of Uno with numPlayers'''
    # set up full deck and initial discard pile
    deck = UnoDeck()
    pile = UnoPile(deck)
    # set up the players
    playerList = []

    computers = int(input(f'How many computers would you like to play with? Or, you can watch a computer game by typing {numPlayers}. '))
    while computers > numPlayers:
        computers = int(input(f'Please pick a number of computers up to {numPlayers}. '))
    
    for n in range(numPlayers - computers):
        # get each player's name, then create an UnoPlayer
        name = input('Player #' + str(n + 1) + ', enter your name: ')
        playerList.append(UnoPlayer(name, deck))

    for n in range(computers):
        playerList.append(UnoPlayer("Cpu " + str(n+ 1), deck, True))

    # randomly assign who goes first
    currentPlayerNum = random.randrange(numPlayers)


    # play the game
    increment = 1  # Added variable to track the play direction
    
    while True:

        skip = False
        # print the game status
        print('-------')
        for player in playerList:
            print(player)
        print('-------\n')

        

        
        time.sleep(1)

        nextPlayerNum = (currentPlayerNum + increment) % numPlayers #Finds index of next playrer 


        # take a turn
        playerList[currentPlayerNum].take_turn(deck, pile)
                
        top_card = pile.top_card() #Assigns top card to variable

        if len(playerList[currentPlayerNum].hand) == 1:
            print('\nUNO!\n')
            time.sleep(5)

        # check for a winner
        if playerList[currentPlayerNum].has_won():
            print("\n" + playerList[currentPlayerNum].get_name() + " wins!\n")
            print("Thanks for playing!")
            break

            
            

        if top_card.rank == 'skip' and top_card.status == 'enabled':
            if playerList[nextPlayerNum].is_cpu():
                print(f'{playerList[nextPlayerNum].get_name()}, your turn has been skipped!\n')
            else:
                print(f"{playerList[nextPlayerNum].get_name()}'s turn has been skipped!\n") 
            time.sleep(2.5)
            skip = True #Increments by one to skip player's turn
            top_card.status = 'disabled'

        elif top_card.rank == 'reverse' and top_card.status == 'enabled':
            print(f'{playerList[currentPlayerNum].get_name()} has reversed the order of the game!\n')
            increment *= -1 #Order of incrementation switched
            top_card.status = 'disabled'
            time.sleep(2.5)


             
        elif top_card.rank == 'wild' and top_card.status == 'enabled':
            
            if not playerList[currentPlayerNum].is_cpu():
                choice_color = ''
                while choice_color not in ['red', 'yellow', 'green', 'blue']:
                    choice_color = input(f'{playerList[currentPlayerNum].get_name()}, what color would you like to choose? (yellow, green, blue, red) ')
                    if choice_color in ['red', 'yellow', 'green', 'blue']:
                        confirm_choice = input(f'Please confirm that the color is {choice_color}. Type enter to proceed, and anything else to cancel. ')
                        if confirm_choice == '':
                            top_card.color = choice_color
                        else:
                            print(f'Okay, choice of {choice_color} canceled.\n')

            
                  
            if playerList[currentPlayerNum].is_cpu():
                color_dict = {'green': 0, 'red': 0, 'yellow': 0, 'blue': 0}
                for card in playerList[currentPlayerNum].hand:
                    if card.color in color_dict:
                        color_dict[card.color] += 1

                best_color = None
                best_count = 0
                for color in color_dict:
                    if color_dict[color] > best_count:
                        best_count = color_dict[color]
                        best_color = color
                
                if sum(color_dict.values()) == 0:
                    colors = ['red', 'yellow', 'green', 'blue']
                    number = random.randint(0, 3)
                    random_color = colors[number]
                    print(f'{playerList[currentPlayerNum].get_name()} chooses {random_color} for the wild card.')
                else:
                    top_card.color = best_color
                    print(f'{playerList[currentPlayerNum].get_name()} chooses {best_color} for the wild card.')
                time.sleep(4)
            
            top_card.status = 'disabled'                   
                           
        elif top_card.rank == 'wildDrawFour' and top_card.status == 'enabled':

            if not playerList[currentPlayerNum].is_cpu():
                choice_color = ''
                while choice_color not in ['red', 'yellow', 'green', 'blue']:
                    choice_color = input(f'{playerList[currentPlayerNum].get_name()}, what color would you like to choose? (yellow, green, blue, red) ')
                    if choice_color in ['red', 'yellow', 'green', 'blue']:
                        confirm_choice = input(f'Please confirm that the color is {choice_color}. Type enter to proceed, and anything else to cancel. ')
                        if confirm_choice == '':
                            top_card.color = choice_color
                        else:
                            print(f'Okay, choice of {choice_color} canceled.\n')

            
                  
            if playerList[currentPlayerNum].is_cpu():
                color_dict = {'green': 0, 'red': 0, 'yellow': 0, 'blue': 0}
                for card in playerList[currentPlayerNum].hand:
                    if card.color in color_dict:
                        color_dict[card.color] += 1

                best_color = None
                best_count = 0
                for color in color_dict:
                    if color_dict[color] > best_count:
                        best_count = color_dict[color]
                        best_color = color
                
                if sum(color_dict.values()) == 0:
                    colors = ['red', 'yellow', 'green', 'blue']
                    number = random.randint(0, 3)
                    random_color = colors[number]
                    print(f'{playerList[currentPlayerNum].get_name()} chooses {random_color} for the wild card.')
                else:
                    top_card.color = best_color
                    print(f'{playerList[currentPlayerNum].get_name()} chooses {best_color} for the wild card.')
                time.sleep(4)
              

            if playerList[nextPlayerNum].is_cpu():
                print(f'{playerList[nextPlayerNum].get_name()} has to draw four cards. \n')
                    
                print(f'{playerList[nextPlayerNum].get_name()} receives a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                time.sleep(1)
                print(f'{playerList[nextPlayerNum].get_name()} receives a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                time.sleep(1)
                print(f'{playerList[nextPlayerNum].get_name()} receives a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                time.sleep(1)
                print(f'{playerList[nextPlayerNum].get_name()} receives a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                time.sleep(1)
                print(f"\n{playerList[nextPlayerNum].get_name()}'s turn has been skipped.\n")
                time.sleep(3)

            if not playerList[nextPlayerNum].is_cpu():                             
                print(f'{playerList[nextPlayerNum].get_name()}, you have to draw four cards! Sorry.\n')

                input(f'{playerList[nextPlayerNum].get_name()}, press enter to draw your first card. ')
                print(f'You received a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card

                input(f'{playerList[nextPlayerNum].get_name()}, press enter to draw your second card. ')
                print(f'You received a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card

                input(f'{playerList[nextPlayerNum].get_name()}, press enter to draw your third card. ')
                print(f'You received a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card

                input(f'{playerList[nextPlayerNum].get_name()}, press enter to draw your fourth card. ')
                print(f'You received a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                    
                print(f'\n{playerList[nextPlayerNum].get_name()}, your turn has been skipped as well.\n')
                time.sleep(3)
            top_card.status = 'disabled'
                
            skip = True #Increments by one to skip player's turn


        elif top_card.rank == 'drawTwo' and top_card.status == 'enabled':
               

                
            if playerList[nextPlayerNum].is_cpu(): 
                print(f'{playerList[nextPlayerNum].get_name()} has to draw two cards. \n')
                    
                print(f'{playerList[nextPlayerNum].get_name()} receives a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                time.sleep(1)
                print(f'{playerList[nextPlayerNum].get_name()} receives a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                time.sleep(1)
                    
                print(f"\n{playerList[nextPlayerNum].get_name()}'s turn has been skipped.\n")

                time.sleep(3)
                
            elif not playerList[nextPlayerNum].is_cpu():
                print(f'{playerList[nextPlayerNum].get_name()}, you have to draw two cards.\n')

                input(f'{playerList[nextPlayerNum].get_name()}, press enter to draw your first card. ')
                print(f'You received a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                        
                input(f'{playerList[nextPlayerNum].get_name()}, press enter to draw your second card. ')
                print(f'You received a {playerList[nextPlayerNum].draw_card(deck)}.\n')  # Forces player to draw card
                print(f'\n{playerList[nextPlayerNum].get_name()}, your turn has been skipped as well.\n')

            skip = True #Increments by one to skip player's turn

            top_card.status = 'disabled'

        
        
            
        # go to the next player
        if skip:
            currentPlayerNum = (currentPlayerNum + (increment * 2)) % numPlayers
        else:
            currentPlayerNum = (currentPlayerNum + increment) % numPlayers
                

players = int(input('How many players would you like to play? '))

print('\n\n\n')

play_uno(players)


#
