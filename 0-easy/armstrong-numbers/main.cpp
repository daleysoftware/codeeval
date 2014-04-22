#include <iostream>
#include <sstream>
#include <fstream>

int digitCount(unsigned int n)
{
    unsigned int count = 0;

    while (n > 0) {
        count++;
        n /= 10;
    }

    return count;
}

bool isArmstrongNumber(unsigned int n)
{
    int digits = digitCount(n);

    int sum = 0;
    int working = n;

    while (working > 0) {
        int digit = working % 10;
        int multipliedDigit = digit;

        for (int i = 1; i < digits; i++) {
            multipliedDigit *= digit;
        }

        sum += multipliedDigit;
        working /= 10;
    }

    return sum == n;
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

        if (isArmstrongNumber(x)) {
            std::cout << "True" << std::endl;
        } else {
            std::cout << "False" << std::endl;
        }
    }
}
