#include <iostream>
#include <fstream>
#include <ctype.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    while (std::getline(file, line))
    {
        for (int i = 0; i < line.length(); i++) {
            putchar(tolower(line[i]));
        }

        std::cout << std::endl;
    }
}
