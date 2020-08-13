from itertools import permutations, combinations
import enchant  #have to do 'pip install pyenchant'
import time

given_word = input("\nWhat is your word? ")
given_number = int(input("How many letters are you solving for? "))
print("")

''' How to get combination for center length string '''
def combination_words(string, number):

    possible_combination = []

    for char in combinations(string, number):  #getting the combination of a word for certain length
        new = ''.join(char)
        possible_combination.append(new)

    return possible_combination


''' How to check if strings in a set is a word '''
def check_english(array):
    
    english_words = []
    d = enchant.Dict("en_US")

    for word in array:
        if d.check(word) == True:
            english_words.append(word)  #appends words that are in the dictionary 

    print(f"List of {given_number} letter words:")

    if len(english_words) == 0:
        print("none")
        
    if len(english_words) == 1:
        print("{english_word[0]}")

    for index, words in enumerate(english_words):
        if index == 0:
            print(f"{word}, ", end = "")
        elif index != len(english_words) - 1:
            print(f"{words}, ", end = "")  #if not the last words, then print with a comma
        else:
            print(words)  #if it's the last word, then print without a comma

''' How to get permutation of certain letters, then checking if these are english words '''
def permutation_word(array):

    possible_words = set()  #makes an empty set

    for word in combinations:
        for char in permutations(word):  #getting the permutations of the word
            new = ''.join(char)
            possible_words.add(new)  #adding to a set to not have duplicates
    
    return possible_words

start = time.time()
combinations = combination_words(given_word, given_number)
words = permutation_word(combinations)
check_english(words)
time = time.time() - start
print(f"\n-----{time} seconds-----\n")


