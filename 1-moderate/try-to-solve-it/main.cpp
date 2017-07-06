#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <map>

static const std::map<char, int> m1 = {
        {'a', 0},
        {'b', 1},
        {'c', 2},
        {'d', 3},
        {'e', 4},
        {'f', 5},
        {'g', 6},
        {'h', 7},
        {'i', 8},
        {'j', 9},
        {'k', 10},
        {'l', 11},
        {'m', 12},
};
static const char v1[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'};

static const std::map<char, int> m2 = {
        {'u', 0},
        {'v', 1},
        {'w', 2},
        {'x', 3},
        {'y', 4},
        {'z', 5},
        {'n', 6},
        {'o', 7},
        {'p', 8},
        {'q', 9},
        {'r', 10},
        {'s', 11},
        {'t', 12},
};
static const char v2[] = {'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't'};

std::string decode(std::string s)
{
    std::ostringstream result;

    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (m1.find(c) != m1.end()) {
            result << v2[m1.at(c)];
        } else {
            result << v1[m2.at(c)];
        }
    }

    return result.str();
}

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    bool first = true;
    while (std::getline(file, line))
    {
        std::cout << decode(line) << std::endl;
    }
}
