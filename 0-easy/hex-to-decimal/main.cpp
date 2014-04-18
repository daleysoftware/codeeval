#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    while (std::getline(file, line))
    {
        unsigned int x;   
        std::stringstream ss;
        ss << std::hex << line;
        ss >> x;

        std::cout << x << std::endl;
    }
}
