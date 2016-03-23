#include <iostream>
#include <sstream>
#include <string>
#include <fstream>

int main(int argc, char** argv)
{
    std::string line;
    std::ifstream infile(argv[1]);

    while (std::getline(infile, line))
    {
        std::istringstream iss(line);
        int a;
        iss >> a;

        if (a < 7) {
            std::cout << "3" << std::endl;
        } else if (a < 31) {
            std::cout << "3, 7" << std::endl;
        } else if (a < 127) {
            std::cout << "3, 7, 31" << std::endl;
        } else if (a < 2047) {
            std::cout << "3, 7, 31, 127" << std::endl;
        } else {
            std::cout << "3, 7, 31, 127, 2047" << std::endl;
        }
    }
}
