#Written by Narnillian, almost entirely on January 19, 2021.
#Mostly copied from the code of the full game I made, which is in the same directory of this Github repo
#When I updated the game on Jan. 20 and 22, I also updated here
#Written in response to cassidoo's "Interview question of the week" from Newsletter #231, Jan. 16 2022

#Make sure to run `python3 -i`

from random import choice

def wordleGuess(guess, solution=None):
    if not solution:
        solution = solution_word
    guessed_word = guess.lower()
    if len(guessed_word) != 5:
        print("Please make sure your guess has exactly 5 letters."); return
    for letter in guessed_word:
        if letter not in alphabet:
            print("Please make sure all the letters in your guess are in the 26 letter English alphabet")
    copy_of_solution = solution
    for letter in range(5):
        if guessed_word[letter] == copy_of_solution[letter]:
            print("🟩", end="")
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ', 1) #i thank you my friend, onmert, for this line
            continue
        elif guessed_word[letter] in copy_of_solution:
            print("🟨", end="")
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ', 1) #i thank you my friend, onmert, for this line
            continue
        else:
            print("⬜", end="")
            continue
    print()

alphabet = "abcdefghijklmnopqrstuvwxyz"
solutions = ["fudge", "party", "parks", "guess", "solve", "print", "debug", "rules", "great", "thing", "write", "reply",
                "these", "stuff", "looks", "jocks", "jumbo", "fuzzy", "pizza", "baker", "cabin", "earth", "words", "might",
                "every", "match", "green", "sound", "could", "trier", "peppy", "apple", "power", "robot", "again", "space",
                "pixel", "phone", "bowls", "range"]
solution_word = choice(solutions)
