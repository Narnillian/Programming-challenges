#Written by Narnillian, starting on January 19, 2021. Mostly copied from the code of the full game I made, which is also in this Github repo
#Written in response to cassidoo's "Interview question of the week" from Newsletter #231, Jan. 16 2022

#Make sure to run with `python3 -i` so you can use the function
def wordleGuess(guess, solution):
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
