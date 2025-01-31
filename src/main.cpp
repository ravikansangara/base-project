#include <cstring>
#include <iostream>

#include "helper.h"
#include "libone.h"
#include "libtwo.h"

void example_buffer_overflow()
{
    char buffer[10];

    // CodeQL will flag this as writing beyond the buffer's capacity
    strcpy(buffer, "This is too long for buffer");
}

int main()
{
    std::cout << "Hello, World!" << std::endl;

    std::cout << "Hello, World-2!" << std::endl;

    helper_function_one();

    libone_function();

    libtwo_function();

    // Functions to test CodeQL quality
    example_buffer_overflow();

    return 0;
}
