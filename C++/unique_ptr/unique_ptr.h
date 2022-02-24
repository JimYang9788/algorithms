#include <iostream>
#include <algorithm>
template <typename T>
class UniquePointer
{
public:
    // constructor
    UniquePointer<T>(T *ptr) : d_ptr(ptr)
    {
    }
    UniquePointer<T>() : d_ptr(nullptr) {}

    // destructor
    ~UniquePointer()
    {
        delete d_ptr;
    }

    // Move Assignment
    UniquePointer<T> &operator=(UniquePointer &&ptr)
    {
        std::cout << "Move Assignment Called" << std::endl;
        std::swap(ptr.getPtr(), d_ptr);
    }

    // Move Constructor
    UniquePointer<T>(UniquePointer &&ptr) : d_ptr(ptr.getPtr())
    {
        std::cout << "Move Constructor Called" << std::endl;
        ptr.setPtr(nullptr);
    }

    // Accessor
    T
        *
        getPtr()
    {
        return d_ptr;
    }

    void setPtr(T *ptr)
    {
        d_ptr = ptr;
    }

private:
    T *d_ptr;
};