# About
The assignment was to just make a function to tell you the result of your guess. I made the whole game, and then copied and pasted some of it into another file with just the function. The two versions get a bit more different from each other every version because the changes have to be done in different ways.

Almost the entire game was finished on January 19, 2022, with a tiny adjustment on the morning of January 20. This adjustment fixed reporting double letters (i.e. "apple" --> "parks" and vice versa) when the word was not entirely correct. I also edited on January 22 to make sure all letters are in the standard English 26 character alphabet. An edit (which I thought was final) was made on January 24. This version added a display of used characters similar to the keyboard in the standard Wordle, and shows that letters have either not been used, or the most correct usage of them (i.e. not in the word, in the word but wrong position, etc.). On January 28, I updated the character display. I added a white highlight (and black text color) for letters that are not used, and changed how the display is output. Each update also added words to the word list.

You can play the original Wordle [here](https://www.powerlanguage.co.uk/wordle/), once per day: https://www.powerlanguage.co.uk/wordle/.

# Details

My full game script has couple of notable differences from the original Wordle. Firstly, I can't stop you from playing more than once per day. Also, since I can't interact with or measure time, there's a random word from a list each time you play, even if the two rounds are right after each other. The final difference that I can think of, in the official Wordle, you can only guess real words from the list. My version lets you guess any combination of 5 letters.

The file with just the function is much more simple. You run `python3 -i [wordle-function.py]` to define the function and leave the Python interface open. Then, you simply call the function with `wordleGuess(["guess"],["solution"])`. It uses basically the same code as the full game script, so everything that applies there applies to this one too.

&nbsp;  
&nbsp;  

## I was mentioned in the newsletter!
![image](https://user-images.githubusercontent.com/94580999/151125291-948be757-536e-48f4-b5ad-ad6214ff2c15.png)
