#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);
    std::string line;

    while (std::getline(file, line))
    {
        int age;   
        std::stringstream ss(line);
        ss >> age;

        // Print line depending on the age.
        if (age < 0 || age > 100) {
            std::cout << "This program is for humans" << std::endl;
            continue;
        }

        if (age <= 2) {
            std::cout << "Still in Mama's arms" << std::endl;
        } else if (age <= 4) {
            std::cout << "Preschool Maniac" << std::endl;
        } else if (age <= 11) {
            std::cout << "Elementary school" << std::endl;
        } else if (age <= 14) {
            std::cout << "Middle school" << std::endl;
        } else if (age <= 18) {
            std::cout << "High school" << std::endl;
        } else if (age <= 22) {
            std::cout << "College" << std::endl;
        } else if (age <= 65) {
            std::cout << "Working for the man" << std::endl;
        } else {
            std::cout << "The Golden Years" << std::endl;
        }
    }
}
