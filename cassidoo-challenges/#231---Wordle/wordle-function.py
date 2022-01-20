#Written by Narnillian, also entirely on January 19, 2021. It wasn't that hard, because it was mostly copied from the code of the full game I made, which is also in this Github repo
#Written in response to cassidoo's "Interview question of the week" from Newsletter #231, Jan. 16 2022

#Make sure to run `python3 -i`

from random import choice

def wordleGuess(guess, solution=None):
    if not solution:
        solution = solution_word
    if len(guess) != 5:
        print("Please make sure your guess has exactly 5 letters.")
    guessed_word = guess.lower()
    copy_of_solution = solution
    for letter in range(5):
        if guessed_word[letter] == copy_of_solution[letter]:
            print("🟩", end="")
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ', 1) #i thank you my friend, Onmert, for this line
            continue
        elif guessed_word[letter] in copy_of_solution:
            print("🟨", end="")
            copy_of_solution = copy_of_solution.replace(guessed_word[letter], ' ') #i thank you my friend, Onmert, for this line
            continue
        else:
            print("⬜", end="")
            continue
    print()

solutions = ["fudge", "party", "parks", "guess", "solve", "print", "debug", "rules", "great", "thing", "write", "reply", "these", "stuff", "looks", "jocks", "jumbo", "fuzzy", "pizza", "baker", "cabin", "earth", "words", "might", "every", "match", "green", "sound", "could", "trier", "peppy", "apple", "power", "robot"]
solution_word = choice(solutions)
