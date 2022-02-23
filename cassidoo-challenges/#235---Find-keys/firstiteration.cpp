#include <iostream>
using namespace std;


int main(int argc, char** argv) {
    string top_row = "qwertyuiop"; //10 letters
    string home_row = "asdfghjkl"; //9 letters
    string bottom_row = "zxcvbnm"; //7 letters
    string keyboard_rows[] = {top_row, home_row, bottom_row};
    char previous_letter;
    int previous_row = 0;
    int previous_keyboard_letter = 0;
    string direction;

    string given_word = "dessert";
    if (argv[1]) {
        given_word = argv[1];
    }


    for (auto &&word_letter : given_word) {

        for (int row = 0; row < 3; row++) {
            for (auto row_letter = 0; row_letter < keyboard_rows[row].length(); row_letter++) {
                if (keyboard_rows[row][row_letter] == word_letter) {
                    if (row - previous_row < 0) { direction = "up"; }
                    else { direction = "down"; }
                    for (int i = 0; i < abs(row - previous_row); i++) {
                        cout << direction << ", ";
                    }

                    if (row_letter - previous_keyboard_letter < 0) { direction = "left"; }
                    else { direction = "right"; }
                    for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                        cout << direction << ", ";
                    }

                    cout << "select, ";

                    previous_letter = word_letter;
                    previous_row = row;
                    previous_keyboard_letter = row_letter;
                    continue;
                }
            }
            
        }

    previous_letter = given_word[word_letter];
    }

    

    cout << "\033[D\033[D  \n";
    


    return 0;
}
