#include <iostream>
#include <sstream>
#include <fstream>

int sumOfDigits(int x)
{
    int sum = 0;
    while (x > 0) {
        sum += x % 10;
        x /= 10;
    }
    return sum;
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

        std::cout << sumOfDigits(x) << std::endl;
    }
}
