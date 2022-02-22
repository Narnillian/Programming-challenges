#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    char top_row[] = "qwertyuiop"; //10 letters
    char home_row[] = "asdfghjkl"; //9 letters
    char bottom_row[] = "zxcvbnm"; //7 letters
    char* keyboard_rows[] = {top_row, home_row, bottom_row};
    char previous_letter;
    char* previous_row = keyboard_rows[0];
    int previous_keyboard_letter = 0;
    string direction;

    string given_word = "dessert";
    if (argv[1]) {
        given_word = argv[1];
    }

    for (auto &&word_letter : given_word) {
        
        if (previous_row == keyboard_rows[0]) {

            int row_letter;
            for (auto &&row : keyboard_rows) {
                for (row_letter = 0; row_letter < strlen(row); row_letter++) {
                    if (row[row_letter] == word_letter) {
                        //give directions
                        if (row_letter - previous_keyboard_letter < 0) { direction = "left"; }
                        else { direction = "right"; }
                        for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                            cout << direction << ", ";
                        }
                        cout << "select, ";


                        previous_row = keyboard_rows[];
                        continue;
                    }
                }
                cout << "down, ";
            }
        } else if (previous_row == keyboard_rows[1]) {
            
        } else {

        }
        

    }
    

    return 0;
}
