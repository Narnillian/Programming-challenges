#include <iostream>
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
        found = false;
        if (word_letter == previous_letter) {
            cout << "\nsamechar"; //this is for reference
            cout << "select, ";
            continue;
        }
        else { rows_moved = 0; }
        if (previous_row == keyboard_rows[0]) {
            cout << "\ntop row"; //this is for reference
            for (auto &&row : keyboard_rows) {
                for (row_letter = 0; row_letter < row.length(); row_letter++) {
                    if (row[row_letter] == word_letter) {
                        //give directions
                        cout << "  {" << row_letter << "}  ";
                        cout << "  {" << previous_keyboard_letter << "}  ";
                        if (row_letter - previous_keyboard_letter < 0) { direction = "left"; } else { direction = "right"; }
                        for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                            cout << direction << ", ";
                        }
                        cout << "select, ";

                        previous_letter = word_letter;
                        found = true;
                        break;
                    }
                }
                if (found) {
                    break;
                }
                cout << "down, ";
                rows_moved++;
            }
        } else if (previous_row == keyboard_rows[1]) {
            cout << "\nhome row";
            for (row_letter = 0; row_letter < home_row.length(); row_letter++) {
                if (home_row[row_letter] == word_letter) {
                    if (row_letter - previous_keyboard_letter < 0) { direction = "left"; } else { direction = "right"; }
                    for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                        cout << direction << ", ";
                    }
                    cout << "select, ";
                    
                    previous_row = keyboard_rows[1];
                    previous_letter = word_letter;
                    found = true;
                    break;
                }
            }
            if (!found) {
                for (row_letter = 0; row_letter < top_row.length(); row_letter++) {
                    if (top_row[row_letter] == word_letter) {
                        cout << "  {" << row_letter << "}  ";
                        cout << "  {" << previous_keyboard_letter << "}  ";
                        cout << "up, ";
                        if (row_letter - previous_keyboard_letter < 0) { direction = "left"; } else { direction = "right"; }
                        for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                            cout << direction << ", ";
                        }
                        cout << "select, ";
                        
                        previous_row = keyboard_rows[0];
                        previous_letter = word_letter;
                        found = true;
                        break;
                    }
                }
            }
            if (!found) {
            for (row_letter = 0; row_letter < bottom_row.length(); row_letter++) {
                if (bottom_row[row_letter] == word_letter) {
                    cout << "down, ";
                    if (row_letter - previous_keyboard_letter < 0) { direction = "left"; } else { direction = "right"; }
                    for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                        cout << direction << ", ";
                    }
                    cout << "select, ";
                    
                    previous_row = keyboard_rows[2];
                    previous_letter = word_letter;
                    break;
                }
            }
            }
        } else {
            cout << "\nbottom row";
            for (auto &&row : reverse_keyboard_rows) {
                for (row_letter = 0; row_letter < row.length(); row_letter++) {
                    if (row[row_letter] == word_letter) {
                        //give directions
                        if (row_letter - previous_keyboard_letter < 0) { direction = "left"; } else { direction = "right"; }
                        for (int i = 0; i < abs(row_letter - previous_keyboard_letter); i++) {
                            cout << direction << ", ";
                        }
                        cout << "select, ";

                        previous_letter = word_letter;
                        found = true;
                        break;
                    }
                }
                if (found) {
                    break;
                }
                cout << "up, ";
                rows_moved++;
            }
        }
        previous_row = keyboard_rows[rows_moved];
        previous_keyboard_letter = row_letter;
    }


    cout << "\033[D\033[D  \n";
    return 0;
}
