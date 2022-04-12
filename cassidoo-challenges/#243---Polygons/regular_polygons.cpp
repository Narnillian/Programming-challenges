#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
    int sides = 0;
    bool findIAS = true;
    bool findIAM = true;
    bool findEAM = true;
    bool findDiags = true;
    string argument;
    float intAngSum = 0;
    float intTheta = 0;
    float extTheta = 0;
    float diagonals = 0;

    if (argc > 2) {
        findIAS = false;
        findIAM = false;
        findEAM = false;
        findDiags = false;
        for (int readArgument = 1; readArgument < argc; readArgument++) {
            argument = argv[readArgument];
            //lowercase:
            for (int i = 0; i < argument.length(); i++) {
                argument[i] = tolower(argument[i]);
            }

            try {
                sides = stoi(argument);
                continue;
            } catch (invalid_argument) {
                //will continue with the code below -- i dont like having it all in this block
            }
            
            if (argument == "intanglesum" || argument == "interioranglesum" || argument == "ias") {
                //cout << "ias\n";
                findIAS = true;
            } else if (argument == "intanglemeasure" || argument == "interioranglemeasure" || argument == "iam") {
                //cout << "iam\n";
                findIAM = true;
            } else if (argument == "extanglemeasure" || argument == "exterioranglemeasure" || argument == "eam") {
                //cout << "eam\n";
                findEAM = true;
            } else if (argument == "diagonals" || argument == "diags") {
                //cout << "diags\n";
                findDiags = true;
            } else {
                try {
                    sides = stoi(argument);
                } catch (invalid_argument) {
                    cout << argument << " is not a valid argument\n\n";
                }
            }
        }
    } else {
        try {
            sides = stoi(argv[1]);
        } catch (invalid_argument) {
            cout << argv[1] << " is not a valid number of sides\n\n";
        }
    }

    if (sides < 3) {
        cout << "Please make sure that you give a valid number of sides for a polygon\n";
        return 0;
    }


    //get interior angle sum of regular polygon with given number of sides
    if (findIAS) {
        intAngSum = (sides-2)*180; //this should never actually be a decimal, but has to be float so the math will work correctly later
        cout << "Interior angle sum of a regular polygon with " << sides << " sides:\033[80G" << intAngSum << "\n";
    }


    //get measure of one interior angle
    if (findIAM) {
        intTheta = intAngSum/sides;
        cout << "Measure of one interior angle of a regular polygon with " << sides << " sides:\033[80G" << intTheta << "\n";
    }

    
    //get measure of one exterior angle
    if (findEAM) {
        extTheta = 360/sides;
        cout << "Measure of one exterior angle of a regular polygon with " << sides << " sides:\033[80G" << extTheta << "\n";
    }


    //get number of diagonals
    if (findDiags) {
        float diagonals = (sides*(sides-3))/2;
        cout << "Number of diagonals in a regular polygon with " << sides << " sides:\033[80G" << diagonals << "\n";
    }


    return 0;
}