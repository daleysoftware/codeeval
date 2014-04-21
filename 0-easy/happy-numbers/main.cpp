#include <iostream>
#include <sstream>
#include <fstream>
#include <set>

int sumOfDigitSquares(int x)
{
    int sum = 0;
    while (x > 0) {
        int lastDigit = x % 10;
        sum += lastDigit * lastDigit;
        x /= 10;
    }
    return sum;
}

bool isNumberHappy(int n)
{
    std::set<int> visited;

    while (visited.find(n) == visited.end()) {
        visited.insert(n);
        n = sumOfDigitSquares(n);

        if (n == 1) {
            return true;
        }
    }

    return false;
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

        std::cout << isNumberHappy(x) << std::endl;
    }
}
