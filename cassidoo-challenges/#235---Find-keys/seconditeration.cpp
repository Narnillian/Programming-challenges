#include <iostream>
//#include <cstring>
using namespace std;

int main(int argc, char** argv) {
    string top_row = "qwertyuiop"; //10 letters
    string home_row = "asdfghjkl"; //9 letters
    string bottom_row = "zxcvbnm"; //7 letters
    string keyboard_rows[] = {top_row, home_row, bottom_row};
    string reverse_keyboard_rows[] = {bottom_row, home_row, top_row};
    char previous_letter = '*';
    string previous_row = keyboard_rows[0];
    int previous_keyboard_letter = 0;
    int rows_moved = 0;
    int row_letter;
    bool found = false;
    string direction;

    string given_word = "dessert";
    if (argv[1]) {
        given_word = argv[1];
    }

    for (auto &&word_letter : given_word) {
        
        if (word_letter == previous_letter) {
            cout << "select, ";
        } else if (previous_row == keyboard_rows[0]) {
            cout << "\ntop row"; //this is for reference
            for (auto &&row : keyboard_rows) {
                for (row_letter = 0; row_letter < row.length(); row_letter++) {
                    if (row[row_letter] == word_letter) {
                        //give directions
                        if (row_letter - previous_keyboard_letter < 0) { direction = "left"; }
                        else { direction = "right"; }
                        for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                            cout << direction << ", ";
                        }
                        cout << "select, ";

                        previous_row = keyboard_rows[rows_moved];
                        previous_letter = word_letter;
                        found = true;
                        break;
                    }
                }
                cout << "down, ";
                rows_moved++;
            }
        } else if (previous_row == keyboard_rows[1]) {
            cout << "\nhome row";
            for (row_letter = 0; row_letter < home_row.length(); row_letter++) {
                if (home_row[row_letter] == word_letter) {
                    if (row_letter - previous_keyboard_letter < 0) { direction = "left"; }
                    else { direction = "right"; }
                    for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                        cout << direction << ", ";
                    }
                    cout << "select, ";
                    
                    previous_row = keyboard_rows[rows_moved];
                    previous_letter = word_letter;
                    break;
                }
            }
            for (row_letter = 0; row_letter < top_row.length(); row_letter++) {
                if (top_row[row_letter] == word_letter) {
                    cout << "up, ";
                    if (row_letter - previous_keyboard_letter < 0) { direction = "left"; }
                    else { direction = "right"; }
                    for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                        cout << direction << ", ";
                    }
                    cout << "select, ";
                    
                    previous_row = keyboard_rows[rows_moved];
                    previous_letter = word_letter;
                    break;
                }
            }
            for (row_letter = 0; row_letter < bottom_row.length(); row_letter++) {
                if (bottom_row[row_letter] == word_letter) {
                    cout << "down, ";
                    if (row_letter - previous_keyboard_letter < 0) { direction = "left"; }
                    else { direction = "right"; }
                    for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                        cout << direction << ", ";
                    }
                    cout << "select, ";
                    
                    previous_row = keyboard_rows[rows_moved];
                    previous_letter = word_letter;
                    break;
                }
            }
        } else {
            cout << "\nbottom row";
            for (auto &&row : reverse_keyboard_rows) {
                for (row_letter = 0; row_letter < row.length(); row_letter++) {
                    if (row[row_letter] == word_letter) {
                        //give directions
                        if (row_letter - previous_keyboard_letter < 0) { direction = "left"; }
                        else { direction = "right"; }
                        for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                            cout << direction << ", ";
                        }
                        cout << "select, ";

                        previous_row = keyboard_rows[rows_moved];
                        previous_letter = word_letter;
                        break;
                    }
                }
                cout << "up, ";
                rows_moved++;
            }
        }
    }

    return 0;
}
