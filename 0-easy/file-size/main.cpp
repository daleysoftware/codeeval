#include <sys/stat.h>
#include <iostream>

int main(int argc, char** argv)
{
    struct stat st;
    stat(argv[1], &st);
    std::cout << st.st_size << std::endl;
}
