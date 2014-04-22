#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

std::string decToBin(unsigned int number)
{
    if (number == 0) return "0";
    if (number == 1) return "1";

    if (number % 2 == 0) {
        return decToBin(number / 2) + "0";
    } else {
        return decToBin(number / 2) + "1";
    }
}

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    while (std::getline(file, line))
    {
        unsigned int x;   
        std::stringstream ss(line);
        ss >> x;

        std::cout << decToBin(x) << std::endl;
    }
}
