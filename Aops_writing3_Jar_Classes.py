# Python Class 3962
# Lesson 3 Problem 5
# Author: origamibuilder (521817)

class Jar:
    '''Creates a jar with a set capacity'''
    
    def __init__(self, capacity):
        '''Jar(capacity) -> Jar
        Constructs a jar
        capacity: int gives filling capacity of the jar.'''
        
        self.capacity = capacity #Sets predefined jar capacity
        
        self.fillStatus = 0 #Jar starts out empty

    def __str__(self):
        '''str(Jar) -> str
        Returns string that tells user how many liters of water the jar has.'''

        if self.fillStatus == 1:
            double_or_single = 'liter'
        else:
            double_or_single = 'liters'

        
        return f'The {str(self.capacity)}-liter jar has {str(self.fillStatus)} {double_or_single} of water.\n'


    def empty(self):
        '''Jar.empty()
        Completely empties jar'''

        self.fillStatus = 0 #Empties jar

        return print(f'{str(self.capacity)}-liter Jar emptied.\n')

    def fill(self):
        '''Jar.fill()
        Completely fills jar'''

        self.fillStatus = self.capacity #Completely fills jar 

        return print(f'{str(self.capacity)}-liter Jar filled.\n')

    def pour(self, other):
        '''Jar.pour(other)  
        Pours water from one jar into another jar until the jar being filled reaches its capacity 
        or until the jar that is pouring water runs out of water unless it is empty or unless the 
        jar that is being filled is already full.
        '''

        if self.fillStatus == 0:
            return print('This jar is empty.\n') #Special case
        
        if other.capacity == other.fillStatus: #Special case
            return print('The jar that you are trying to pour water into is already full.\n')

        pour_capacity = other.capacity - other.fillStatus

        #How much water before the jar is full 


        if pour_capacity < self.fillStatus: #If less than the amount of water in the pouring jar 

            
            other.fillStatus += pour_capacity #Adds water

            self.fillStatus -= pour_capacity #Takes away water
            
            return print(f'Water poured into {str(other.capacity)}-liter jar until its max capacity was reached.\n')

        else:

            other.fillStatus += self.fillStatus #Adds water from jar 

            self.fillStatus = 0 #Empty 

            return print(f'Water poured into the {str(other.capacity)}-liter jar until the {str(self.capacity)}-liter jar ran out of water.\n') 
            
        
fiveJar = Jar(5) #Creates 5-liter jar

threeJar = Jar(3) #Creates 3-liter jar

print(fiveJar)

print(threeJar)

fiveJar.fill() #5-liter full, 3-liter empty

fiveJar.pour(threeJar) #5-liter has 2 liters, 3-liter full

threeJar.empty() 

fiveJar.pour(threeJar) #5-liter empty, 3-liter has 2 liters

fiveJar.fill() 

fiveJar.pour(threeJar) #5-liter has 4 liters, 3-liter full

threeJar.empty()

print(fiveJar) #5-liter has 4-liters

print(threeJar) #3-liter empty



'''
Technical Score: 7 / 7
Style Score: 0.9 / 1
Comments:
Great work solving this week's problem and finding the solution for the puzzle, origamibuilder!

The first step in solving this problem is to correctly implement the $\verb#Jar#$ class. Here, you did a good job adding all the necessary attributes and implementing the required set of functions.

However, writing
return print
when you want one of the class' methods to print something is not a good practice. Notice that returning a value and printing something to the console are different actions. When you use$\verb# return print(...)#$, the function will effectively return $\verb#None#$ because $\verb#print()#$ function itself returns $\verb#None#$. This is fine, as functions don't necessarily have to return anything, they can just perform actions, such as filling or emptying a jar. But since those functions are not returning anything already, using just a $\verb#print#$ statement would be sufficient and more appropriate.

As a suggestion, you could include an option to let the user create jars that are partially filled already. To do that, introduce a new parameter to the $\verb#__init__#$ method and set that parameter to a default of 0, like this:
def __init__(self, capacity, fillStatus=0):
    self.capacity=capacity
    self.fillStatus = fillStatus

If we call this constructor with $\verb#Jar(5)#$, it will create a jar with capacity $5$ and automatically set $\verb#fillStatus#$ to zero. But if we provide a value for $\verb#fillStatus#$ by writing $\verb#Jar(5,3)#$, it will create a $5$-liter jar with $3$ liters of water in it.

As you've noticed, the AoPS Python widget doesn't support $\verb#f-strings#$. However, you should still use them, as they make your code way more concise and readable. We always run your code in Idle when grading your work, so as long as it works there, you're good. The AoPS built-in Python widget is great for short coding exercises, but for the following homework problems you will be better served with a Integrated Development Environment.

Once you had the $\verb#Jar()#$ class ready, the next part was to find the solution to the puzzle. For this, you've correctly found a series of steps to end up with exactly 4 liters of water in the 5-liter jar. Printing the status of each jar after each step made it easier to follow your strategy!

Regarding coding style, using inline comments and docstrings for each function, as well as descriptive and helpful variable names, you’ve made your code easy to read and understand. This ensures it can be easily edited in the future, whether that’s by you or by someone else. Keep it up and keep working hard!

Your Response:
__init__: Creates a jar with a capacity that is set by the user that has no water in it.

__str__: Just returns the jar capacity and how much water it has.

Empty: Just sets the amount of water in the jar to 0.

Fill: Sets the amount of water in the jar to its max capacity.

Pour: This method was the most complex out of all the methods. The reason that this is more complicated than the other methods is because we have to account for two different scenarios:
(1) The jar that is pouring water into the other jar runs out of water
(2) The jar that is being filled with water reaches its max capacity

This is why I created a variable (pour_capacity) that tests for how much water the jar that is being poured into can carry before it reaches its max capacity. If this amount is less than the amount of water available in the jar that is pouring water, then we need to stop pouring before the jar overflows. Else, we just empty the first jar and add all of this water to the other jar, which is why an if else statement is needed for this method.

Note: F-strings just return parse errors in this browser so this needs to be run in IDLE.
'''
