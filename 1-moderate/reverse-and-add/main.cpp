#include <iostream>
#include <sstream>
#include <fstream>

unsigned int reverseDigits(unsigned int num)
{
    unsigned int rev = 0;
    while (num > 0)
    {
      unsigned int dig = num % 10;
      rev = rev * 10 + dig;
      num /= 10;
    }

    return rev;
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

        unsigned int iterations = 0;
        while (true) {
            unsigned int reverse = reverseDigits(x);
            if (reverse == x) {
                std::cout << iterations << " " << x << std::endl;
                break;
            }

            iterations++;
            x = x + reverse;
        }
    }
}
