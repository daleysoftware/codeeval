#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    int sum = 0;
    while (std::getline(file, line))
    {
        int x;   
        std::stringstream ss(line);
        ss >> x;
        sum += x;
    }

    std::cout << sum << std::endl;
}
