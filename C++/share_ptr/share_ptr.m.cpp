#include "share_pointer.h"
#include <utility>
#include <memory>
#include <iostream>

int main()
{
    // SharePointer<int> sp2(new int);
    SharePointer<int> sp1(new int);
    SharePointer<int> sp3(std::move(sp1));
    sp1 = sp3;
    sp1 = std::move (sp3);
}