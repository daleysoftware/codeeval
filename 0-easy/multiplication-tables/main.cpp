#include <iostream>
#include <iomanip>

int main(int argc, char** argv)
{
    for (int i = 1; i <= 12; i++) {
        for (int j = 1; j <= 12; j++) {
            std::cout << std::setfill(' ') << std::setw(4) << (i*j);
            
        }
        std::cout << std::endl;
    }
}
