# About
The assignment was to just make a function to tell you the result of your guess. I made the whole game, and then copied and pasted some of it into another file with just the function.

Almost the entire game was finished on January 19, 2022, with a tiny adjustment on the morning of January 20. (This adjustment fixed reporting double letters [i.e. "apple" --> "parks" and vice versa] when the word was not entirely correct). I also edited on January 22 to make sure all letters are in the standard English 26 character alphabet.

You can play the original Wordle [here](https://www.powerlanguage.co.uk/wordle/), once per day: https://www.powerlanguage.co.uk/wordle/.

# Details

My full game script has couple of notable differences from the original Wordle. Firstly, I can't stop you from playing more than once per day. Also, since I can't interact with or measure time, there's a random word from a list each time you play, even if the two rounds are right after each other. The final difference that I can think of, in the official Wordle, you can only guess real words from the list. My version lets you guess any combination of 5 letters.

The file with just the function is much more simple. You run `python3 -i [wordle-function.py]` to define the function and leave the Python interface open. Then, you simply call the function with `wordleGuess([guess],[solution])`. It uses basically the same code as the full game script, so everything that applies there applies to this one too.
