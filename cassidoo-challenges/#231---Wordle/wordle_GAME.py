#Written in its entirety on January 18, 2022
#Written by Narnillian, in response to cassidoo's "Interview question of the week" from Newsletter #231, Jan. 16 2022

from random import choice
from sys import argv

#for debugging (duh):
if len(argv) > 1:
    debug = argv[1]
else: debug = False

#setup
victory = False
solutions = ["fudge", "party", "parks", "wordl", "wrdle", "guess", "solve", "print", "debug", "rules", "great", "thing", "write", "reply", "these", "stuff", "looks", "jocks", "jumbo", "fuzzy", "pizza", "baker", "cabin", "earth"]
if debug:
    for i in solutions:
        matches = 0
        if len(i) != 5:
            print(f"\n{i} has more than 5 letters!")
            print(f"{i} has more than 5 letters!\n")
        for j in solutions:
            if i == j:
                matches += 1
        if matches > 1:
            print(f"\n{i} is in the list more than once!")
            print(f"{i} is in the list {matches} times!\n")
solution_word = choice(solutions)
print("I have a word!")

#gameplay
while not victory:
    correct = 0
    while True:
        guessed_word = input("Please guess my word: ")
        if len(guessed_word) == 5:
            break
        print("Guess must be 5 letters!\n")
    guessed_word = guessed_word.lower()
    for letter in range(5):
        if guessed_word[letter] == solution_word[letter]:
            print("🟩", end="")
            correct += 1
        elif guessed_word[letter] in solution_word:
            print("🟨", end="")
        else:
            print("⬜", end="")
    print()
    if correct == 5:
        victory = True
    #just for dev process:
    if debug:
        if not victory:
            print(solution_word)
    print("")
print("Correct! You have guessed the word!")
print(f"The word was: {solution_word}")
