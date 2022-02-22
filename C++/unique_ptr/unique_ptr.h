#include <iostream>

class UniquePointer
{
public:
    UniquePointer() : a(1) {}
    void Print() { std::cout << "sup" << std::endl; }

private:
    int a;
};