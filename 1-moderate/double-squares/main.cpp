#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>

unsigned int countDoubleSquares(unsigned int x)
{
    if (x == 0) {
        return 1;
    }

    unsigned int result = 0;

    for (unsigned int b = 0; b <= pow(x, 0.5); b++) {
        unsigned int a = pow(x - pow(b, 2), 0.5);

        if (a < b) {
            break;
        }

        if (x == (pow(a ,2) + pow(b, 2))) {
            result++;
        }
    }

    return result;
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

        if (first) {
            // Skip the number of lines count.
            first = false;
            continue;
        }

        std::cout << countDoubleSquares(x) << std::endl;
    }
}
