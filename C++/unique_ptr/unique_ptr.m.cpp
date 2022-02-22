#include "unique_ptr.h"
#include <iostream>
int main()
{
    std::cout << "hello world" << std::endl;
    UniquePointer u = UniquePointer();
    u.Print();
}
