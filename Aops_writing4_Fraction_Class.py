# Python Class 3962
# Lesson 4 Problem 6
# Author: origamibuilder (521817)

class Fraction:
    '''represents fractions'''

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError

        self.num = num 

        self.denom = denom


    def __str__(self):
        '''str(Fraction) -> str
        string representation of Fraction'''
        
        return f'{self.num}/{self.denom}'

    def __float__(self):
        '''float(Fraction) -> float
        returns decimal representation of fraction'''
        
        return self.num/self.denom #Returns float 
        
    

    
    def simplify(self):
        '''Fraction.simplify() -> None
        Fully simplifies fraction'''

        if self.num == 0: #If the numerator is 0, make the fraction 0/1
            self.denom = 1
            self.num = 0
            return

        smallerNum = min(abs(self.num), abs(self.denom)) #Finds smaller number find simplifying

        simplStatus = True
        while simplStatus == True: #Until a fraction can no longer be simplified, simplify it

            for num in range(1, int(smallerNum) + 1): #For every number from 1 to smaller number
                
                if self.num % num == 0 and self.denom % num == 0 and num != 1:
                    #If both the numerator and denominator are divisible by a number
                    self.num /= num #Divide num by number
                    self.denom /= num #Divide denom by number
                    smallerNum /= num #Divide smaller number by number
                    simplStatus = True #Continue loop
                    break
                simplStatus = False #If no number worked, break loop

        if self.denom < 0: #Switches the negative from numerator to the denominator or makes both positive
            self.num *= -1
            self.denom *= -1

        
        self.num = int(self.num)
        self.denom = int(self.denom)

    def lcm(self, other):
        '''Fraction.lcm(Fraction) -> int
        Calculates the least common multiple of two fractions'''
        
        self.simplify()
        other.simplify()
        
        test_num = 1

        while True: 
            if (self.denom * test_num) % other.denom == 0:
                best_lcm = self.denom * test_num
                break #Finds the first multiple of self.denom that other.denom is a factor of

            test_num += 1

        return best_lcm
        
                


    def __mul__(self, other):
        '''Fraction * Fraction -> str
        Returns product of two fractions in string form'''
        
        new_frac = Fraction(self.num * other.num, self.denom * other.denom)
        new_frac.simplify() #Multiplies nums and denoms and then simplifies
        return new_frac

    def __truediv__(self, other):
        '''Fraction/Fraction -> str
        Returns quotient of two fractions in string form'''
        
        new_frac = Fraction(self.num * other.denom, self.denom * other.num)
        #Uses the formula (x/y)/(a/b) = (x/y) * (b/a) and simplifies
        new_frac.simplify()

        return new_frac

        
    def __add__(self, other):
        '''Fraction + Fraction -> str
        Returns sum of two fractions using lcm in string form'''
       
        
        lcm = self.lcm(other) #Finds lcm

        factor = lcm / self.denom

        new_self_num = self.num * factor

        #Multiplies numerator so that fraction's denominator is equivalent to lcm

        factor = lcm / other.denom 

        new_other_num = other.num * factor

        #Does the same for the other fraction

        new_frac = Fraction(new_self_num + new_other_num, lcm) #Adds the numerators

        new_frac.simplify() #Simplifies

        return new_frac

    def __sub__(self, other):
        '''Fraction - Fraction -> str
        Returns difference of two fractions using lcm in string form'''
        
        
        lcm = self.lcm(other)

        factor = lcm / self.denom

        new_self_num = self.num * factor

         #Multiplies numerator so that fraction's denominator is equivalent to lcm


        factor = lcm / other.denom 

        new_other_num = other.num * factor

        #Does the same for the other fraction

        new_frac = Fraction(new_self_num - new_other_num, lcm)

        new_frac.simplify() #Subtracts numerators and simplifies

        return new_frac

    def __eq__(self, other):
        '''Fraction == Fraction -> bool
        Calculates and returns whether two fractions are equal'''
        
        self.simplify() 
        other.simplify()

        #Simplifies both fractions

        if self.num == other.num and self.denom == other.denom:
            return True #If both numerators and denominators are equal return True

        return False #Else return False
    


        
        
p = Fraction(3,6)
p.simplify()
print(p)  # should print 1/2
q = Fraction(10,-60)
q.simplify()
print(q)  # should print -1/6
r = Fraction(-24,-48)
r.simplify()
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5

### if overloading using special methods
print(p+q)  # should print 1/3
print(p-q)  # should print 2/3
print(p-p)  # should print 0/1
print(p*q)  # should print -1/12
print(p/q)  # should print -3/1
print(p==r) # should print True
print(p==q) # should print False


"""
Technical Score: 6 / 7
Style Score: 0.8 / 1
Comments:
Good work, origamibuilder! Your $\verb#Fraction#$ class uses its two attributes, $\verb#num#$ and $\verb#denom#$, to store the information it needs, and you’ve implemented the required methods for displaying fractions and doing arithmetic.

However, notice that the $\verb#__str__()#$ method should display the fraction in the lowest possible terms, even if we didn't explicitly call the $\verb#simplify()#$ method before, as you did when you you were testing your code:
p = Fraction(3,6)
p.simplify()
print(p)

We should be able to get $\verb#'1/2'#$ by calling just
p = Fraction(3,6)
print(p)
We can accomplish this by calling the $\verb#simplify()#$ method within the $\verb#__str__()#$ method:
def __str__(self):
        '''str(Fraction) -> str
        string representation of Fraction'''
        self.simplify()
        return f'{self.num}/{self.denom}'

Even better, you could call the $\verb#simplify()#$ method within the class constructor, so that when a fraction is created it is automatically simplified.

Notice that you don't really need the $\verb#lcm()#$ method to add and subtract fractions. Instead, you can just "cross-multiply" and use $\verb#self.denominator * other.denominator#$ as the denominator of the new fraction. You are simplifying the result before returning it anyways, so you don't need to worry about introducing common factors on the new fraction.

Finally, you can simplify
if self.num == other.num and self.denom == other.denom:
            return True #If both numerators and denominators are equal return True
 
        return False #Else return False
to just
return self.num == other.num and self.denom == other.denom
If both conditions ($\verb#self.num == other.num#$ and $\verb#self.denom == other.denom#$) are $\verb#True#$, the entire expression we're returning evaluates to $\verb#True#$. If either condition is $\verb#False#$, the entire expression evaluates to $\verb#False#$. By using the simplified return statement, you make your code cleaner and easier to understand.

You've documented your solution thoroughly, using both words in the text box and comments and docstrings in the code itself. This makes your work easy to read and understand, and easy to edit if you come back to it in the future. Keep it up and keep working hard!

Your Response:
__init__: Outputs ZeroDivisionError if denominator is 0. Sets numerator to input numerator. Sets denominator to input denominator.

__str__: Uses simplify() method to simplify the fraction and outputs it in the format "a/b" where a is the numerator and b is the denominator.

__float__: Returns the numerator divided by the denominator.

simplify: This was definitely the hardest method. Firstly, it checks the case for if the numerator is 0 and if so, it just returns the numerator as 0 and the denominator as 1. The method then identifies whether the numerator or the denominator is the greater number, and then, in a while loop, it looks for every factor possible in range of the smaller number and if there are any, it divides the numerator, denominator, and "smallerNum" by that number, and redoes the loop again. If there are no factors in range of the smallerNum, the while loop breaks. The method then makes sure that the negative, if any, is in the numerator, and not the denominator, and then it returns the fraction.

Note: I realize after that I could have just imported math and used the gcd function to simplify the fraction instead but the function works so it's fine.

lcm: Here, self.denom is systematically multiplied at an increment of 1 until it also becomes a multiple of other.denom. This new number that is a multiple of both denominators is the lcm. This number is then returned.

__mul__: Just creates a new fraction by multiplying the two inputted fractions numerators and then denominators, and then it returns this fraction.

__truediv__: Same thing as __mul__, but it uses the formula (x/y)/(a/b) = (x/y) * (b/a) (multiples the first fraction's numerator by the other fraction's denominator and the first fraction's denominator by the other fraction's numerator.

__add__: Uses the lcm method to find the lcm of both inputted fractions, multiples the fractions to match their denominators to equal that lcm, and adds the numerators together to create a new fraction, which is outputted.

__sub__: Same thing as add, but it subtracts the numerators.

__eq__: Simplifies both fractions and tests to see if their numerators and denominators are equal. If they are, output True. Else, output False.
"""



