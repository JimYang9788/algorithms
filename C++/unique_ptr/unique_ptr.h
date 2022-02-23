#include <iostream>

template <typename T>
class UniquePointer
{
public:
    UniquePointer<T>(T *ptr) {}
    UniquePointer<T>() {}

private:
    T *d_ptr;
};