#Written in its entirety on January 19, 2022, with a tiny bit of editing on the 20th and the addition of a character checker (probably unneccesary) on the 22nd
#Also, on the 24th, added a list to show which characters have been used already and fixed the character checker -- before it would break the game
#On 28th -- added highlighting for letters used, but not in the word, and updated system for display of letter information
#There were continual updates to the word list throughout
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
alphabet = "abcdefghijklmnopqrstuvwxyz"
highlight = []
for i in range(26):
    highlight.append(49)
solutions = ["fudge", "party", "parks", "guess", "solve", "print", "debug", "rules", "great", "thing", "write", "reply",
                "these", "stuff", "looks", "jocks", "jumbo", "fuzzy", "pizza", "baker", "cabin", "earth", "words", "might",
                "every", "match", "green", "sound", "could", "trier", "peppy", "apple", "power", "robot", "again", "space",
                "pixel", "phone", "bowls", "range", "super", "light", "inner", "outer", "inter", "false", "check", "added",
                "coder", "goods", "homes", "edits", "packs", "speak", "tests", "bites"]
if debug: #make sure all solutions are good
    for i in solutions:
        matches = 0
        if len(i) != 5:
            print(f"\n{i} does not have 5 letters!")
            print(f"{i} does not have 5 letters!\n")
            exit()
        for j in solutions:
            if i == j:
                matches += 1
        if matches > 1:
            print(f"\n{i} is in the list more than once!")
            print(f"{i} is in the list {matches} times!\n")
            exit()
solution_word = choice(solutions)
print("I have a word!\n")

#gameplay
for i in range(6):
    correct = 0
    copy_of_solution = solution_word
    print(f"\033[46mThis is turn {i+1}/6\033[49m")
    while True: #check guess is 5 letters
        bad_letters = False
        guessed_word = input("Please guess my word: ")
        for letter in guessed_word:
            if letter not in alphabet:
                print("Please make sure all the letters in your guess are in the 26 letter English alphabet\n")
                bad_letters = True
                continue
        if bad_letters:
            pass
        elif len(guessed_word) == 5:
            break
        else:
            print("Guess must be 5 letters!\n")
    guessed_word = guessed_word.lower()
    for letter in range(5):
        lists_index = highlight[alphabet.index(guessed_word[letter])]
        if guessed_word[letter] == copy_of_solution[letter]:
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ', 1) #i thank you my friend, onmert, for this line
            highlight[alphabet.index(guessed_word[letter])] = 42 #replace value at index of letter with color code for green highlight
            print("🟩", end="")
            correct += 1
        elif guessed_word[letter] in copy_of_solution:
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ', 1) #i thank you my friend, onmert, for this line
            if lists_index != 42:
                highlight[alphabet.index(guessed_word[letter])] = 43 #replace value at index of letter with color code for yellow highlight
            print("🟨", end="")
        else:
            highlight[alphabet.index(guessed_word[letter])] = "30;47" #replace value at index of letter with color code for black text, white highlight
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
    print()
    for i in range(26):
        #print each letter with the correct highlighting
        print(f"\033[{highlight[i]}m", end="")
        print(f"{alphabet[i]}", end="")
        print("\033[39;49m", end="")
    print("\n")
if victory:
    print("\nCorrect! You have guessed the word!")
else:
    print("After 6 turns, you could not find the word!")
    print("Fortunately for you, I have no way of stopping you from playing again.")
    print("It will (probably) be a different word though.")
print(f"\nThe word this round was: \"{solution_word}\"")
