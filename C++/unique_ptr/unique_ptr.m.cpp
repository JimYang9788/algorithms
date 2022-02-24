#include "unique_ptr.h"
#include <iostream>
int main()
{
    std::cout << "hello world" << std::endl;
    UniquePointer<int> sp1(new int);
    UniquePointer<int> sp2(std::move(sp1));
}
