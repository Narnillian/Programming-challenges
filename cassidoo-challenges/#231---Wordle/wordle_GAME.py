#Written in its entirety on January 19, 2022, with a tiny bit of editing on the 20th
#Written by Narnillian, in response to cassidoo's "Interview question of the week" from Newsletter #231, Jan. 16 2022
#All code was written by Narnillian, except for where explicitly stated

from random import choice
from sys import argv

#for debugging (duh):
if len(argv) > 1:
    debug = argv[1]
else: debug = False

#setup
victory = False
solutions = ["fudge", "party", "parks", "guess", "solve", "print", "debug", "rules", "great", "thing", "write", "reply",
                "these", "stuff", "looks", "jocks", "jumbo", "fuzzy", "pizza", "baker", "cabin", "earth", "words", "might",
                "every", "match", "green", "sound", "could", "trier", "peppy", "apple", "power", "robot", "again"]
if debug:
    for i in solutions:
        matches = 0
        if len(i) != 5:
            print(f"\n{i} does not have 5 letters!")
            print(f"{i} does not have 5 letters!\n")
        for j in solutions:
            if i == j:
                matches += 1
        if matches > 1:
            print(f"\n{i} is in the list more than once!")
            print(f"{i} is in the list {matches} times!\n")
solution_word = choice(solutions)
print("I have a word!\n")

#gameplay
for i in range(6):
    correct = 0
    copy_of_solution = solution_word
    print(f"This is turn {i+1}/6")
    while True:
        guessed_word = input("Please guess my word: ")
        if len(guessed_word) == 5:
            break
        print("Guess must be 5 letters!\n")
    guessed_word = guessed_word.lower()
    for letter in range(5):
        if guessed_word[letter] == copy_of_solution[letter]:
            print("🟩", end="")
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ', 1) #i thank you my friend, Onmert, for this line
            correct += 1
        elif guessed_word[letter] in copy_of_solution:
            print("🟨", end="")
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ', 1) #i thank you my friend, Onmert, for this line
        else:
            print("⬜", end="")
    print()
    if debug:
        print(f"\"{copy_of_solution}\"")
    if correct == 5:
        victory = True
        break
    #just for dev process:
    if debug:
        print(solution_word)
    print("")
if victory:
    print("\nCorrect! You have guessed the word!")
else:
    print("After 6 turns, you could not find the word!")
    print("Fortunately for you, I have no way of stopping you from playing again.")
    print("It will (probably) be a different word though.")
print(f"The word this round was: {solution_word}")
