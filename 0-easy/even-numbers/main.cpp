#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    while (std::getline(file, line))
    {
        int x;   
        std::stringstream ss(line);
        ss >> x;
        std::cout << ((x & 0x01) == 0 ? 1 : 0) << std::endl;
    }
}
