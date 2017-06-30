#include <iostream>
#include <sstream>
#include <fstream>

unsigned int countPossibleNecklaceArrangements(unsigned int beads)
{
    return 0;
}


int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    bool first = true;
    while (std::getline(file, line))
    {
        unsigned int x;   
        std::stringstream ss(line);
        ss >> x;

        std::cout << countPossibleNecklaceArrangements(x) << std::endl;
    }
}
