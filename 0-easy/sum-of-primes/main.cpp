#include <iostream>
#include <math.h>

bool isPrime(int n)
{
    int root = (int) sqrt(n);

    for (int i = 2; i <= root; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

int main(int argc, char** argv)
{
    unsigned int sum = 0;
    unsigned int primesSummed = 0;
    unsigned int currentNumber = 2;

    while (primesSummed < 1000) {
        if (isPrime(currentNumber)) {
            sum += currentNumber;
            primesSummed++;
        }

        currentNumber++;
    }

    std::cout << sum << std::endl;
}
