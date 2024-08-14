# Python Class 3962
# Lesson 1 Problem 7
# Author: origamibuilder (521817)

def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''

    plaintext = list(plaintext)
    
    new_text = ''
    

    
    for rail_num in range((numRails - 1), -1, -1): #For every rail 

        rail_text = ''
        
        num_char = rail_num #Increments by rail_num and stops right before it exceeds the length of plaintext
        while num_char <= len(plaintext):
            
            if num_char > (len(plaintext) - 1):
                break #If it is about to exceed the limit, stop the loop

            rail_text += plaintext[num_char] #Updates the new text 

            num_char += numRails #Increments 
           
            

        new_text += rail_text

    return new_text


def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''

    ciphertext = list(ciphertext) 

    decipher_text = [''] * len(ciphertext) #New list that stores the new values

    

    mod = len(ciphertext) % numRails

    rail_length = int((len(ciphertext) - mod )/ numRails)
    #Finds out how long each rail is without taking into account remainders 
    
    rail_lengths = [rail_length] * numRails
    #Creates a new list to store the length of each rail, now accounting remainders

    for residuals in range(mod):
        rail_lengths[residuals] += 1

    
    
  
    char_num = 0 #Used as a placeholder for searching ciphertext

    for rails in range(numRails -1, -1, -1):
        #Searches the rails backwards in order to properly update decipher_text

        for char_length in range(int(rail_lengths[rails])):
            #Searching the list of rail lengths to account for remainders
            if (rails + (char_length * numRails)) >= len(decipher_text):
                break
                #If the list index surpasses the length of the decipher_text, it stops
            decipher_text[rails + (char_length * numRails)] = ciphertext[char_num]
            #Updates decipher_text by searching ciphertext with char_num
            
            char_num += 1 #Increments by one every loop cycle 
            
    decipher_text = ''.join(decipher_text)  
    
            
    return decipher_text

    
def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    
    with open(str(wordfilename), 'r') as input_file:
        valid_words = set(line.strip().lower() for line in input_file)
    '''Opens file and converts it into a set so that the computer doesn't have to keep reading it over and over again.
        Makes sure that everything is lower case and also makes sure that there are no extra lines or spaces'''
    
    #Alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    alphabet = list(alphabet)
    
    best_rail = 0
    
    max_working_words = 0
    
    for rail_possibility in range(1, 1000): #Scans over every possible number of rails from 1-1000
        working_words = 0
        rail = decipher_fence(str(ciphertext), rail_possibility) #Uses decipher_fence function previously made to eliminate redundancies
        rail = list(rail) #Turns inputted text into a list 
        
        
        for char in rail:
            if char not in alphabet: #Takes out all punctuation and everything that is not a space or not in the alphabet
                rail.remove(char)
            
        rail = [char.lower() for char in rail] #Makes every letter in the list lowercase
        rail = ''.join(rail)
        
        rail = rail.split() #Forms words by eliminating all extra spaces

        
        
        for word in rail:
            if word in valid_words:
                working_words += 1
        #Scans to see how many words in the list are real English words (according to wordlist.txt)         
                    
        if working_words > max_working_words:
            max_working_words = working_words
            best_rail = rail_possibility
        #Checks to see if this decipher has the most real English words                      
                        
        
    
    #Returns the best working decipher 
    return decipher_fence(str(ciphertext), best_rail)
           
        
                
    
    

# test cases
print('\nENCODING\n')

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou'
print(encipher_fence("Can you please come over to my house today? Thanks!", 7))

print('\nDECIPHERING\n')

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!
print(decipher_fence("ueo sykos ouanyaetoda em hohnlor tTapcey  !C  vme?s", 7))


print('\nDECODING\n')

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'C:/Users/nisha/Downloads/wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'C:/Users/nisha/Downloads/wordlist.txt'))
# should print... we'll let you find out!
print(decode_text("ueo sykos ouanyaetoda em hohnlor tTapcey  !C  vme?s", 'C:/Users/nisha/Downloads/wordlist.txt'))



'''Technical Score: 7 / 7
Style Score: 0.9 / 1

Comments:

Part (a): Excellent work in this part, origamibuilder! You’ve implemented a function that encrypts a given string using the railfence cipher rules. Using a nested loop you were able to extract the characters of each rail and assemble them in the correct order.

For all your purposes here, converting $\verb#plaintext#$ to a list is not necessary. Strings in Python are iterable, and you can access characters by index directly without needing to convert the string to a list.

As an extra challenge, see if you can find a way to use string slicing to extract the rails instead. Remember the syntax $\verb#list[start:stop:step]#$. For each rail, slice the $\verb#plaintext#$ starting at the rail's index and increment by the number of rails. Give this a try before checking the official solution.

Part (b): Good job with the decryption function as well! The most important insight here is that all of the rails may not have the same length. You successfully determined the length of each rail and extracted the rails from the ciphertext. Once you had the rails extracted, you successfully reversed the steps of encryption. Well done!

Part (c): Well done! Using a loop and your code from part (b), you decrypted the given input with each of the possible numbers of rails, and identified the option that yielded the largest number of valid words. Great job remembering to remove punctuation and convert each word to lowercase.

As in part (a), converting $\verb#alphabet#$ to a list in line 95 is not necessary.

General Comments: Besides the program itself, you've done an excellent job documenting your work in the text box. Describing your work in words has made your solution easier to understand. Very well done!

Regarding coding style, you've followed all the best practices. Picking descriptive names for your variables, including inline comments, and starting each function with a docstring makes the code accessible and easy to read. Keep it up!

Welcome to Intermediate Python! Programming is a valuable skill that requires some unique thinking and a fair amount of patience. We look forward to working with you as you develop your skills and want you to know that we’re always here to help. Feel free to reach out on the class message board any time you want to discuss a problem or one of the other topics from class. Tips.

Let us know if there is anything we can help you with, and keep working hard!'''


'''
Your Response:
Encipher_fence:

For encipher_fence, the idea is to use a loop that runs based on the number of
rails. First, I convert the text into a list. The loop then goes through this
list, jumping by the number of rails each time.For example, in the cipher
"hsi etTi sats.", rail zero is "Ti sats." and rail one is "hsi et". This means
we need to run the loop backwards to get the rails in the correct order.
To ensure that the code doesn’t input an invalid list index,
I use a while loop that stops before the index exceeds the list length.
Overall, this function was not too bad, and I only had to fix a few syntax errors.

Decipher_fence:

Initially, I thought I could reverse the process for decipher_fence the same
way I did for encipher_fence, but I realized that that didn’t work because the
rail fence cipher uses a zigzag pattern. Additionally, since the rails are
already combined, I also had to find a different approach.
After re-examining the examples, though, I noticed a pattern:
we can reconstruct the text by taking characters from each rail in sequence.
For instance, we take the first character from rail zero, then the first from
rail one, and so on. This continues with the second characters,
third characters, etc (displayed by document 1 with one of the examples of
railNum being 3). This helped me internalize that each character in a rail is spaced numRails apart in the deciphered text. I used this pattern for my final code, with a loop for each rail. To handle extra characters (remainders), I created a list (rail_length) that distributes them evenly (as displayed by document 2 which uses an example of if railNum was 6 and there were 32 chars in total). Inside the loop for each rail, another loop checks how many iterations are needed based on these remainders. Like encipher_fence the loop runs backwards to match its encoding process.

Decode_Fence:

For decode_text, I used a loop that runs decipher_fence for rail numbers
from one to one thousand. Inside this loop, I convert the text into a list,
remove punctuation, and make everything lowercase to match wordlist.txt.
Another loop inside checks how many words in the deciphered text are
valid English words. The computer then finds which decipher has the most
valid words and returns it. Initially, this ran really slowly because the
program searched the file every time it looped. To speed it up,
I converted the file into a set before the loop, which made it run much faster.

Note: The code works when I run it in IDLE with a downloaded wordlist.txt file,
but it doesn’t seem to work directly here.
'''
