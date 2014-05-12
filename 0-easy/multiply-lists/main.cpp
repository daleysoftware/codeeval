#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::string line;

    while (std::getline(file, line))
    {
        std::vector<std::string> sv;
        std::stringstream ss(line);
        std::string s;
        while (ss >> s) sv.push_back(s);

        std::vector<int> v1;
        std::vector<int> v2;
        for (int i = 0; i < sv.size()/2; i++) {
            v1.push_back(atoi(sv[i].c_str()));
        }
        for (int i = sv.size()/2 + (sv.size() % 2 == 0 ? 0 : 1); i < sv.size(); i++) {
            v2.push_back(atoi(sv[i].c_str()));
        }

        for (int i = 0; i < v1.size(); i++) {
            std::cout << v1[i] * v2[i];
            if (i+1 != v1.size()) {
                std::cout << " ";
            }
        }

        std::cout << std::endl;
    }
}
