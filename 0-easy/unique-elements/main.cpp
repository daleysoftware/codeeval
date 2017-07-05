#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <fstream>
#include <set>

template <typename Iter>
std::string join(Iter begin, Iter end, std::string const& separator)
{
    std::ostringstream result;

    if (begin != end) {
        result << *begin++;
    }

    while (begin != end) {
        result << separator << *begin++;
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
        std::set<int> s;
        std::stringstream ss(line);

        int i;
        while (ss >> i)
        {
            s.insert(i);
            if (ss.peek() == ',') {
                ss.ignore();
            }
        }

        std::cout << join(s.begin(), s.end(), ",") << std::endl;
    }

}