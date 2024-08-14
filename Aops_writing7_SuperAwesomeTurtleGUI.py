# Python Class 3962
# Lesson 7 Problem 5 Part (b)
# Author: origamibuilder (521817)

import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''

    def __init__(self):

        '''SuperAwesomeTurtle(turtle.Turtle) -> Turtle Window
        Turtle that moves around based on user inputs'''
        
        turtle.Turtle.__init__(self)
        # the getscreen() method returns the Screen object that
        #    the turtle lives in

        self.speed = 0 #Starts out still 
        
        self.getscreen().onkey(self.end,'q') #Exits program

        self.getscreen().onkey(self.stop, 's') #Stops Turtle 
        
        self.getscreen().onkey(self.goforward, 'Up') #Increases turtle speed in the positive direction

        self.getscreen().onkey(self.gobackward, 'Down') #Increases turtle speed in the negative direction

        self.getscreen().onkey(self.turnright, 'Right') #Turns right 90 degrees 

        self.getscreen().onkey(self.turnleft, 'Left') #Turns left 90 degrees

    def goforward(self):
        '''SuperAwesomeTurtle.goforward()  
        Increases turtles forward speed by 1
        Calls move method'''
        
        self.speed += 1 #Speed increases by 1
        self.move() 
        
    def gobackward(self):
        '''SuperAwesomeTurtle.gobackward() 
        Increases turtles backwards speed by 1
        Calls move method'''
        
        self.speed -= 1 #Speed decreases by 1
        self.move()
        
    def move(self):
        '''SuperAwesomeTurtle.move() 
        Turtle moves forward and is called again as soon as timer ends
        Results in infinite loop'''
        
        self.forward(self.speed) #Moves forward fixed number of times
        self.getscreen().ontimer(self.move,40) #After 40 milliseconds, start again

    def turnright(self):
        '''SuperAwesomeTurtle.turnright() 
        Turtle turns right 90 degrees'''

        self.right(90) 

    def turnleft(self):
        '''SuperAwesomeTurtle.turnleft() 
        Turtle turns left 90 degrees'''
        
        self.left(90)
               
    def stop(self):
        '''SuperAwesomeTurtle.stop() 
        Turtle stops'''
        
        self.speed = 0
        

    def end(self):
        '''SuperAwesomeTurtle.end() 
        Closes Window'''
        
        self.getscreen().bye()

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()


'''
Technical Score: 6 / 7
Style Score: 0.8 / 1
Comments:
Good work, origamibuilder!Your $\verb#SuperAwesomeTurtle#$ works well, and you did a great job setting up all of the listeners in the $\verb#__init__#$ function. By adjusting the amount by which the turtle moves forward, you ensure that it has the correct speed at all times.

However, when we try to run your program, we see that sometimes your turtle doesn't behave as expected, for example, moving at an angle instead of following a grid. That happened because you're calling $\verb#self.move()#$ when updating the turtle's speed. Each time you call this method, a new timer is added to update the turtle's position, with causes the off behavior. Instead, it's better to call $\verb#self.move()#$ only once, in the $\verb#__init__#$ method, so that a single timer is running.

Well done documenting your code well! The docstrings at the start of each of your functions clearly identify what they do, and the inline comments add more detail, so that anyone reading or modifying your code will not be confused.

Keep up the hard work!


Your Response:

Code based off of part A

Records turtle's speed using the attribute self.speed. Using the infinite recursive method from part A, self.speed is used as the unit of how fast the turtle is going to go. The move() method also functions with the turtle going backwards.
'''
