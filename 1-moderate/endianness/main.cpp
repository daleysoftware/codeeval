#include <iostream>
#include <stdint.h>

enum
{
    O32_LITTLE_ENDIAN = 0x03020100ul,
    O32_BIG_ENDIAN = 0x00010203ul
};

int main()
{
    static const union {
        unsigned char bytes[4];
        uint32_t value;
    } o32_host_order = { { 0, 1, 2, 3 } };

    if (o32_host_order.value == O32_LITTLE_ENDIAN) {
        std::cout << "LittleEndian" << std::endl;
    } else {
        std::cout << "BigEndian" << std::endl;
    }
}
