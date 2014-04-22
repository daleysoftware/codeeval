#include <iostream>
#include <sstream>
#include <fstream>

int countNumberOfOneBits(unsigned int n)
{
    unsigned int count = 0;

    while (n != 0) {
        unsigned int lastBit = n & 0x1;

        if (lastBit != 0) {
            count++;
        }

        n >>= 1;
    }

    return count;
}

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    while (std::getline(file, line))
    {
        int x;   
        std::stringstream ss(line);
        ss >> x;

        std::cout << countNumberOfOneBits(x) << std::endl;
    }
}
