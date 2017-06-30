#include <iostream>
#include <set>
#include <vector>
#include <sstream>
#include <fstream>

std::set<unsigned int> primes({2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31});

bool isPrime(unsigned int x)
{
    return primes.find(x) != primes.end();
}

unsigned int countPossibleNecklaceArrangements(std::vector<unsigned int> &beads, unsigned int pos)
{
    if (beads.size() == pos) {
        return isPrime(1 + beads[beads.size()-1]) ? 1 : 0;
    }
    unsigned int result = 0;
    if (isPrime(beads[pos] + beads[pos-1])) {
        result += countPossibleNecklaceArrangements(beads, pos+1);
    }
    for (unsigned int i = pos + 2; i < beads.size(); i += 2) {
        if (isPrime(beads[pos-1] + beads[i]))  {
            unsigned int tmp = beads[i];
            beads[i] = beads[pos];
            beads[pos] = tmp;

            result += countPossibleNecklaceArrangements(beads, pos + 1);

            tmp = beads[i];
            beads[i] = beads[pos];
            beads[pos] = tmp;
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

        std::vector<unsigned int> beads;
        for (unsigned int i = 0; i < x; i++) {
            beads.push_back(i+1);
        }

        std::cout << countPossibleNecklaceArrangements(beads, 1) << std::endl;
    }
}
