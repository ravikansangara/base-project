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

void example_uninitialized_variable()
{
    int x;                        // Variable 'x' is not initialized
    std::cout << x << std::endl;  // CodeQL will flag the use of an uninitialized variable
}

void example_memory_leak()
{
    int* ptr = new int[10];
    // No call to delete[] ptr, which CodeQL will detect as a memory leak
}

void example_sql_injection(const std::string& userInput)
{
    std::string query = "SELECT * FROM users WHERE username = '" + userInput + "';";

    // CodeQL will flag this as a potential SQL injection risk
    std::cout << "Executing query: " << query << std::endl;
}

int main()
{
    std::cout << "Hello, World!" << std::endl;

    helper_function_one();

    libone_function();

    libtwo_function();

    // FUnctions to test CodeQL quality
    example_buffer_overflow();
    example_uninitialized_variable();
    example_memory_leak();
    example_sql_injection("Alice");

    return 0;
}
