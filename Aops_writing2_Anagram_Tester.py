# Python Class 3962
# Lesson 2 Problem 4 Part (a)
# Author: origamibuilder (521817)

def anagrams(word):
    '''anagrams(word) -> list
    returns all possible permutations/anagrams of the input word'''

    if len(word) == 0:
        return ['']  # Base case: empty string

    if len(word) == 1:  # Base case: single character
        return [word]

    anagram_list = []

    for i in range(len(word)):
        special_char = word[i]  # Choose the special character
        remaining_word = word[:i] + word[i+1:]  # The remaining characters

        # Get all anagrams of the remaining characters
        subAnagrams = anagrams(remaining_word)

        # Add the special character to the front of each sub-anagram and add to the list
        for anagram in subAnagrams:
            new_anagram = special_char + anagram
            if new_anagram not in anagram_list:  # Ensure uniqueness
                anagram_list.append(new_anagram)

    return anagram_list

def jumble_solve(word):
    '''jumble_solve(word) -> string
    returns all valid words that are anagrams of the word'''
    
    word = anagrams(word) #Uses anagram function 

    valid_word_list = []

    with open('C:/Users/nisha/Downloads/wordlist (1).txt', 'r') as input_file:
        valid_words = set(line.strip().lower() for line in input_file)
    #Creates a set of all the words so that the computer does not have to
    
    for words in word: #Scans list
        words = words.lower()
        if words in valid_words: #If the word is valid, add it to valid_word_list
            valid_word_list.append(words)
            
        
    return valid_word_list

# test cases
print(anagrams('h'))   # should print ['h']
print(anagrams('hi'))  # should print ['hi', 'ih']
print(anagrams('bye')) # should print ['bye', 'bey', 'ybe', 'yeb', 'eby', 'eyb'] in some order


print(jumble_solve('chwat')) #watch
print(jumble_solve('rarom')) #armor
print(jumble_solve('ceplin')) #pencil
print(jumble_solve('yaflim')) #family




'''
Response: Anagram Function:

To understand the anagrams() function, we first need to revisit the permute() function from the part (a). In permute(), after handling base cases, the function iterates through each number in the list, recursively generating and solving the function of the list without this number. Each recursive call returns lists of permutations, and then the number that was taken out before is added back to the beginning of this function. These lists of permutations are then returned.

The anagrams() function operates similarly but deals with a string input instead of a list. To account for the fact that the input is a list for permute() and is a string for anagrams(), I needed to replace some list operations like .pop() with string slicing (word[:i] + word[i+1:]) to remove characters and using appropriate variable names like remaining_word instead of subList.

Jumble Solve Function:

The jumble_solve() function is much more straightforward. Initially, it just uses the anagrams() function to generate all possible anagrams of a given word. Just like I did in writing problem 1 (railfence cipher), I created a set (valid_words) from the wordlist.txt file so that the computer does not have to keep on opening the file and slow down.

During debugging, the only issues I faced were special cases, such as the case where a user's input has a capitalized letter and it needed to be lowercased, which is why I did words = words.lower().

The final step involved iterating through the list of generated anagrams (word) and checking each against valid_words. Valid matches were appended to valid_word_list, which is then returned as the result.


Note: Like the last writing problem, this problem does not work for me when run here, but it works when I run it in IDLE.




Technical Score: 7 / 7
Style Score: 1 / 1
Comments:
Good job solving this week's problem, origamibuilder! By modifying the permute() function, you created a recursive function that finds all the anagrams of a given string. Good job ensuring that duplicates are not included in the final list.

Including a base case for when the inputted string has length 1 makes your program slightly more efficient, since it avoids a few extra recursive calls. However, including this second base case is not strictly necessary, since the main loop can also handle it.

Your jumble_solve() function also works well. As a suggestion, consider making the file containing the list of valid words an argument of that function. This would allow users to solve jumble puzzles in different contexts effortlessly. For instance, if someone wants to solve jumble puzzles in Paris, they could simply load a file containing a list of French words into your function, rather than having to modify line 41 of your code.

In terms of coding style, you've done a great job making your code accessible and easy to understand by picking descriptive names for your variables, including inline comments, and starting each function with a docstring. You've also done an excellent job describing your process in the textbox. Keep it up and keep working hard!
'''
