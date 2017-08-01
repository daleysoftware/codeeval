#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

int OFFSET = (int) 'A';

std::string convertToExcelColumnName(int number)
{
    number--;
    std::vector<char> result;

    while (number >= 0) {
        int quotient = number / 26;
        int remainder = number % 26;
        result.push_back((char) (OFFSET + remainder));
        number = quotient - 1;
    }

    std::stringstream ss;

    for(std::vector<char>::reverse_iterator it = result.rbegin(); it != result.rend(); ++it) {
        ss << *it;
    }

    return ss.str();
}

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;
    bool first = true;
    while (std::getline(file, line))
    {
        std::istringstream reader(line);
        int val;
        reader >> val;

        std::cout << convertToExcelColumnName(val) << std::endl;
    }
}
